import re
import base64
import json
import struct
from sys import stdout
import time
import urllib.parse
#from pyftdi.i2c import I2cController

class Animation(object):
    __slots__ = ("speed", "delay", "direction", "repeat", "data",
        # only informational, not stored in EEPROM
        "name")

    def __init__(self, data=b"", **kwargs):
        self.speed = 13
        self.delay = 0
        self.direction = 0
        self.repeat = 1  # default in web editor is 0=infinite
        self.data = data
        self.name = ""

        for k,v in kwargs.items():
            setattr(self, k, v)

    @property
    def type(self):
        raise Exception("abstract method")

    def __repr__(self):
        return "%s(%r, speed=%d, delay=%d, direction=%d, repeat=%d, name=%r)" % (
            type(self).__name__,
            self.data, self.speed, self.delay, self.direction, self.repeat, self.name)

    @staticmethod
    def from_url(url):
        m = re.match(r"^(?:https?://)?editor[.]blinkenrocket[.]de/[?]s=([-_a-zA-Z0-9+/%]+(%3D)*)$", url)
        if not m:
            raise Exception("invalid URL")
        encoded = urllib.parse.unquote(m.group(1))
        encoded = encoded.replace("%3D", "=").replace("%2B", "+").replace("%2F", "/").replace("-", "+").replace("_", "/")
        decoded = base64.b64decode(encoded)
        #print(b"DEBUG: " + decoded)
        info = json.loads(decoded)

        if "delay" in info:
            info["delay"] = round(2 * info["delay"])

        info2 = info.copy()
        for k in "id,creationDate,modifiedAt,text,animation,type".split(","):
            if k in info2:
                del info2[k]

        if info["type"] == "text":
            return TextAnimation(info["text"], **info2)
        elif info["type"] == "pixel":
            return PixelAnimation(info["animation"]["data"], **info2)
        else:
            raise Exception("type of animation is not supported")

    def to_url(self):
        info = {"delay": self.delay * 0.5, "repeat": self.repeat, "direction": self.direction, "name": self.name, "speed": self.speed}
        if self.type == 1:
            info["type"] = "text"
            info["animation"] = {"currentFrame": 0, "length": 1, "frames": 1}
            info["text"] = str(self.data, "ascii")
        elif self.type == 2:
            info["type"] = "pixel"
            info["animation"] = {"currentFrame": 0, "length": int(len(self.data)/8), "frames": int(len(self.data)/8), "data": list(self.data)}
        else:
            raise Exception("invalid type: %r" % (self.type,))
        #print("DEBUG: " + json.dumps(info))
        return "editor.blinkenrocket.de/?s=" + urllib.parse.quote(base64.b64encode(bytes(json.dumps(info), "ascii")))

    @property
    def header_bytes(self):
        # see https://github.com/blinkenrocket/firmware/blob/master/utilities/blinkenrocket.py#L161
        if len(self.data) >= (1<<12):
            raise Exception("animation has too much data")
        return struct.pack(">H",
            self.type << 12 | len(self.data))

    @property
    def frame_header_bytes(self):
        raise Exception("abstract method")

    def to_bytes(self):
        return self.header_bytes + self.frame_header_bytes + self.data

    @staticmethod
    def from_bytes(data):
        type_and_len, header1, header2 = struct.unpack_from(">HBB", data)
        payload = data[4:4+(type_and_len & 0xfff)]
        if type_and_len >> 12 == 1:
            return TextAnimation.from_bytes(header1, header2, bytes(payload))
        elif type_and_len >> 12 == 2:
            return PixelAnimation.from_bytes(header1, header2, bytes(payload))
        else:
            raise Exception("invalid animation")

    @staticmethod
    def to_eeprom(*anims):
        if len(anims) >= 255:
            raise Exception("too many animations")
        eeprom = bytearray(b"\xff"*256)
        eeprom[0] = len(anims)

        page_offset = 0
        for i, anim in enumerate(anims):
            anim_bytes = anim.to_bytes()
            eeprom[1+i] = page_offset
            startaddr = 256 + 32*page_offset
            endaddr = startaddr + len(anim_bytes)
            if len(eeprom) < endaddr:
                eeprom += b"\xff"*(endaddr - len(eeprom))
            eeprom = eeprom[0:startaddr] + anim_bytes + eeprom[endaddr:]
            # next animation starts on next page boundary after endaddr
            page_offset = int((endaddr - 256 + 31)/32)

        return eeprom

    @staticmethod
    def from_eeprom(eeprom):
        if eeprom[0] == 255:
            return []
        anims = []
        for page_offset in eeprom[1:1+eeprom[0]]:
            startaddr = 256 + 32*page_offset
            length = struct.unpack_from(">H", eeprom, offset=startaddr)[0]
            anims.append(Animation.from_bytes(eeprom[startaddr:startaddr+4+length]))
        return anims

class TextAnimation(Animation):
    __slots__ = ()

    def __init__(self, text, **kwargs):
        if type(text) == str:
            text = bytes(text, "ascii")
        else:
            text = bytes(text)
        super().__init__(data=text, **kwargs)

    @property
    def type(self):
        return 1

    @property
    def frame_header_bytes(self):
        return struct.pack(">BB",
            self.speed << 4 | self.delay,
            self.direction << 4 | self.repeat)

    @classmethod
    def from_bytes(cls, header1, header2, payload):
        # see https://github.com/blinkenrocket/firmware/blob/master/src/system.cc#L82
        return cls(payload, speed=header1>>4, delay=header1&0xf, direction=header2>>4, repeat=header2&0xf)

class PixelAnimation(Animation):
    __slots__ = ()

    def __init__(self, *frames, **kwargs):
        data = b""
        for frame in frames:
            if type(frame) == str:
                frame = frame.strip("\r\n")
                if len(frame) != 64+7:
                    raise Exception("frame has invalid length: %r" % ((len(frame), 64+7, frame),))
                rows = frame.split("\n")
                if len(rows) != 8:
                    raise Exception("frame must have exactly 8 rows: %r" % (rows,))
                value = {' ': 0, 'X': 1}
                xs = [sum(value[rows[row][col]] << (7-row) for row in range(8)) for col in range(8)]
                data += bytes(xs)
            elif len(frame) % 8 == 0:
                data += bytes(frame)
            else:
                raise Exception("invalid frame")
        super().__init__(data=data, **kwargs)

    @property
    def type(self):
        return 2

    @property
    def frame_header_bytes(self):
        return struct.pack(">BB", self.speed&0xf, self.delay<<4 | self.repeat)

    @classmethod
    def from_bytes(cls, header1, header2, payload):
        # see https://github.com/blinkenrocket/firmware/blob/master/src/system.cc#L82
        return cls(payload, speed=header1&0xf, delay=header2>>4, repeat=header2&0xf, direction=0)

    def __repr__(self):
        frames = ""
        if len(self.data)%8 != 0:
            frames = "%r," % (self.data,)
        else:
            chars = " X"
            for i in range(int(len(self.data)/8)):
                frame = self.data[8*i:8*i+8]
                frames += "\n\t# %d" % i
                frames += " +".join("\n\t\"" + "".join(chars[(frame[col]>>(7-row))&1] for col in range(8)) + "\" + \"\\n\"" for row in range(8)) + ","
        return "%s(%s\n\tspeed=%d, delay=%d, repeat=%d, name=%r)" % (
            type(self).__name__,
            frames,
            self.speed, self.delay, self.repeat, self.name)

    def play(self):
        if len(self.data)%8 != 0:
            raise Exception("invalid frame data")
        else:
            print("\n\n\n\n\n\n\n\n")
            chars = " X"
            for i in range(int(len(self.data)/8)):
                frame = self.data[8*i:8*i+8]
                print("\r\x1b[8A" + "\r\n".join(
                    "".join(chars[(frame[col]>>(7-row))&1] for col in range(8)) for row in range(8)))
                stdout.flush()

                # Delay after the animation is set to 244. This is supposed to be 0.5 sec.
                # Speed is 250 - 16*speed.
                time.sleep(0.5/244 * (250-16*self.speed))

            time.sleep(0.5*self.delay)

class I2cEEPROM(object):
    __slots__ = ("ftdi", "eeprom_address", "other_address")

    def __init__(self, ftdi_conn_string="ftdi://ftdi:232h/1", eeprom_address=0x50, other_address=0x10):
        self.eeprom_address = eeprom_address
        self.other_address = other_address
        from pyftdi.i2c import I2cController
        self.ftdi = I2cController()
        self.ftdi.configure(ftdi_conn_string)

    def check_i2c_is_working(self, repeat=1):
        import pyftdi.i2c
        # We often get into a state with the bus pulled low. This is particularly annoying because the master will see
        # this as a valid ack. We try to read from an invalid address, which should cause a NACK.
        for i in range(repeat):
            if i > 0:
                time.sleep(0.1)
            try:
                self.ftdi.read(self.other_address, 0)
                stdout.write(".")
                stdout.flush()
            except pyftdi.i2c.I2cNackError:
                return
        raise Exception("We get an ACK for other_address so the I2C bus seems to be broken (permanently pulled low).")

    #NOTE The EEPROM on my blinkenrocket seems to be 64kbits, not 256kbits. That doesn't really matter. If we read too much,
    #     we will merely get the same data again.
    #def read_eeprom(self, size=int(256*1024/8), start=0):
    def read_eeprom(self, size=int(64*1024/8), start=0):
        self.check_i2c_is_working()
        self.ftdi.write(self.eeprom_address, [start>>8, start&0xff])
        return self.ftdi.read(self.eeprom_address, size)

    def write_eeprom(self, data, start=0):
        page_size = 32
        data = bytes(data)
        i = 0
        while i < len(data):
            #print(self.ftdi.get_gpio().read())
            self.check_i2c_is_working(10)
            print("writing EEPROM at 0x%04x: %r" % ((start+i), data[i:i+page_size]))
            self.ftdi.write(self.eeprom_address, bytes([(start+i)>>8, (start+i)&0xff]) + data[i:i+page_size])
            i += page_size

