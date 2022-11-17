#! /usr/bin/env nix-shell
#! nix-shell -i python -p "python3.withPackages(p:[p.pyftdi])"

# editor.blinkenrocket.de/?s=eyJkZWxheSI6MCwicmVwZWF0IjowLCJkaXJlY3Rpb24iOjAsImlkIjoiNTM5MTc5ZWUtNGFkNi00MDE0LTllMjAtNmFlYTRlYTEwOWZlIiwibmFtZSI6IiIsInNwZWVkIjo5LCJjcmVhdGlvbkRhdGUiOjE2NjY5MDgwMTYsInR5cGUiOiJwaXhlbCIsImFuaW1hdGlvbiI6eyJkYXRhIjpbMzEsMjEsMTcsMCwzMCwxLDMwLDAsMjEsMTcsMCwzMCwxLDMwLDAsOCwxNywwLDMwLDEsMzAsMCw4LDMxLDAsMzAsMSwzMCwwLDgsMzEsMCwzMCwxLDMwLDAsOCwzMSwwLDgsMSwzMCwwLDgsMzEsMCw4LDMxLDMwLDAsOCwzMSwwLDgsMzEsMCwwLDgsMzEsMCw4LDMxLDAsMjksOCwzMSwwLDgsMzEsMCwyOSwyMSwzMSwwLDgsMzEsMCwyOSwyMSwxOCwwLDgsMzEsMCwyOSwyMSwxOCwwLDgsMzEsMCwyOSwyMSwxOCwwLDE0LDMxLDAsMjksMjEsMTgsMCwxNCw4MSwwLDI5LDIxLDE4LDAsMTQsODEsODEsMjksMjEsMTgsMCwxNCw4MSw4MSw3OCwyMSwxOCwwLDE0LDgxLDgxLDc4LDY0LDE4LDAsMTQsODEsODEsNzgsNjQsODAsMCw3OCw4MSw4MSw3OCw2NCw4MCw4OCw3OCw4MSw4MSw3OCw2NCw4MCw4OCw4MCw4MSw4MSw3OCw2NCw4MCw4OCw4MCwyMDgsODEsNzgsNjQsODAsODgsODAsMjA4LDgwLDc4LDY0LDgwLDg4LDgwLDIwOCw4MCwwLDMyLDQ4LDU2LDQ4LDQ4LDQ4LDExMiwzMiwxNiwyNCwxNiwxNiwxNiwxNiw0OCwxNiwxMiw4LDgsOCw4LDgsOCwyNCw4LDgsOCwwLDAsOCw4LDgsOCw4LDAsMCwwLDAsOCw4LDgsMCwwLDAsMCwwLDAsOCwwLDAsMCwwLDAsMCwwLDBdLCJjdXJyZW50RnJhbWUiOjI4LCJsZW5ndGgiOjI5LCJmcmFtZXMiOjI5fSwibW9kaWZpZWRBdCI6IjIwMjItMTAtMjdUMjI6MTY6NDQuNzI2WiJ9
# 
# 
# editor.blinkenrocket.de/?s=eyJkZWxheSI6MCwicmVwZWF0IjowLCJkaXJlY3Rpb24iOjAsImlkIjoiNTM5MTc5ZWUtNGFkNi00MDE0LTllMjAtNmFlYTRlYTEwOWZlIiwibmFtZSI6IiIsInNwZWVkIjo5LCJjcmVhdGlvbkRhdGUiOjE2NjY5MDgwMTYsInR5cGUiOiJwaXhlbCIsImFuaW1hdGlvbiI6eyJkYXRhIjpbMzEsMjEsMTcsMCwzMCwxLDMwLDAsMjEsMTcsMCwzMCwxLDMwLDAsOCwxNywwLDMwLDEsMzAsMCw4LDMxLDAsMzAsMSwzMCwwLDgsMzEsMCwzMCwxLDMwLDAsOCwzMSwwLDgsMSwzMCwwLDgsMzEsMCw4LDMxLDMwLDAsOCwzMSwwLDgsMzEsMCwwLDgsMzEsMCw4LDMxLDAsMjksOCwzMSwwLDgsMzEsMCwyOSwyMSwzMSwwLDgsMzEsMCwyOSwyMSwxOCwwLDgsMzEsMCwyOSwyMSwxOCwwLDgsMzEsMCwyOSwyMSwxOCwwLDE0LDMxLDAsMjksMjEsMTgsMCwxNCw4MSwwLDI5LDIxLDE4LDAsMTQsODEsODEsMjksMjEsMTgsMCwxNCw4MSw4MSw3OCwyMSwxOCwwLDE0LDgxLDgxLDc4LDY0LDE4LDAsMTQsODEsODEsNzgsNjQsODAsMCw3OCw4MSw4MSw3OCw2NCw4MCw4OCw3OCw4MSw4MSw3OCw2NCw4MCw4OCw4MCw4MSw4MSw3OCw2NCw4MCw4OCw4MCwyMDgsODEsNzgsNjQsODAsODgsODAsMjA4LDgwLDc4LDY0LDgwLDg4LDgwLDIwOCw4MCwwLDMyLDQ4LDU2LDQ4LDQ4LDQ4LDExMiwzMiwxNiwyNCwxNiwxNiwxNiwxNiw0OCwxNiwxMiw4LDgsOCw4LDgsOCwyNCw4LDgsOCwwLDAsOCw4LDgsOCw4LDAsMCwwLDAsOCw4LDgsMCwwLDAsMCwwLDAsOCwwLDAsMCwwLDAsMCwwLDAsMCwwLDAsMCwwLDgsMCwwLDAsMCwwLDAsMTIsMTIsMCwxMiwwLDAsMCwzMCwzMCwwLDMwLDAsMCwwLDMxLDMxLDAsMCwzMSwwLDAsMzEsMzEsMjEsMCwzMCwzMSwwXSwiY3VycmVudEZyYW1lIjozMywibGVuZ3RoIjozNCwiZnJhbWVzIjozNH0sIm1vZGlmaWVkQXQiOiIyMDIyLTEwLTI3VDIyOjIyOjU3LjE2NloifQ%3D%3D
# {"delay":0,"repeat":0,"direction":0,"id":"539179ee-4ad6-4014-9e20-6aea4ea109fe","name":"","speed":9,"creationDate":1666908016,"type":"pixel","animation":{"data":[31,21,17,0,30,1,30,0,21,17,0,30,1,30,0,8,17,0,30,1,30,0,8,31,0,30,1,30,0,8,31,0,30,1,30,0,8,31,0,8,1,30,0,8,31,0,8,31,30,0,8,31,0,8,31,0,0,8,31,0,8,31,0,29,8,31,0,8,31,0,29,21,31,0,8,31,0,29,21,18,0,8,31,0,29,21,18,0,8,31,0,29,21,18,0,14,31,0,29,21,18,0,14,81,0,29,21,18,0,14,81,81,29,21,18,0,14,81,81,78,21,18,0,14,81,81,78,64,18,0,14,81,81,78,64,80,0,78,81,81,78,64,80,88,78,81,81,78,64,80,88,80,81,81,78,64,80,88,80,208,81,78,64,80,88,80,208,80,78,64,80,88,80,208,80,0,32,48,56,48,48,48,112,32,16,24,16,16,16,16,48,16,12,8,8,8,8,8,8,24,8,8,8,0,0,8,8,8,8,8,0,0,0,0,8,8,8,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,12,12,0,12,0,0,0,30,30,0,30,0,0,0,31,31,0,0,31,0,0,31,31,21,0,30,31,0],"currentFrame":33,"length":34,"frames":34},"modifiedAt":"2022-10-27T22:22:57.166Z"}
# editor.blinkenrocket.de/?s=eyJkZWxheSI6MCwicmVwZWF0IjowLCJkaXJlY3Rpb24iOjAsImlkIjoiMGU2MzQ2MWQtNTVhZC00MzM3LWIwYmUtZjdlMDYzYThmM2FjIiwibmFtZSI6IiIsInNwZWVkIjoxMywiY3JlYXRpb25EYXRlIjoxNjY2OTA5NjQyLCJ0eXBlIjoidGV4dCIsInRleHQiOiIgIEpldHp0IGthbm5zdCBkdSBuaWNodCBtZWhyIGJlaGF1cHRlbiwgZGFzcyBkdSBuaWNodCBsb2V0ZW4ga2FubnN0IiwiYW5pbWF0aW9uIjp7ImRhdGEiOlswLDAsMCwwLDAsMCwwLDBdLCJjdXJyZW50RnJhbWUiOjAsImZyYW1lcyI6MSwibGVuZ3RoIjoxfSwibW9kaWZpZWRBdCI6IjIwMjItMTAtMjdUMjI6Mjc6MjQuMzkwWiJ9
# {"delay":0,"repeat":0,"direction":0,"id":"0e63461d-55ad-4337-b0be-f7e063a8f3ac","name":"","speed":13,"creationDate":1666909642,"type":"text","text":"  Jetzt kannst du nicht mehr behaupten, dass du nicht loeten kannst","animation":{"data":[0,0,0,0,0,0,0,0],"currentFrame":0,"frames":1,"length":1},"modifiedAt":"2022-10-27T22:27:24.390Z"}
# editor.blinkenrocket.de/?s=eyJkZWxheSI6MCwicmVwZWF0IjowLCJkaXJlY3Rpb24iOjAsImlkIjoiMTQ5MDgwNzYtODNjNy00MmIwLTliOGYtZWU1YjY1ZTI4YWY3IiwibmFtZSI6IiIsInNwZWVkIjo1LCJjcmVhdGlvbkRhdGUiOjE2NjY5MDk2NDksInR5cGUiOiJwaXhlbCIsImFuaW1hdGlvbiI6eyJkYXRhIjpbMCwxOTYsMTk0LDE4LDE4LDE5NCwxOTYsMCwwLDY4LDY2LDE4LDE4LDE5NCwxOTYsMF0sImN1cnJlbnRGcmFtZSI6MCwibGVuZ3RoIjoyLCJmcmFtZXMiOjJ9LCJtb2RpZmllZEF0IjoiMjAyMi0xMC0yN1QyMjozMDo1NS4zMzdaIn0%3D
# {"delay":0,"repeat":0,"direction":0,"id":"14908076-83c7-42b0-9b8f-ee5b65e28af7","name":"","speed":5,"creationDate":1666909649,"type":"pixel","animation":{"data":[0,196,194,18,18,194,196,0,0,68,66,18,18,194,196,0],"currentFrame":0,"length":2,"frames":2},"modifiedAt":"2022-10-27T22:30:55.337Z"}
# 
# 
# {"delay":0,"repeat":0,"direction":0,"id":"539179ee-4ad6-4014-9e20-6aea4ea109fe","name":"","speed":9,"creationDate":1666908016,"type":"pixel","animation":{"data":[0,0,0,0,0,8,0,0,0,0,0,0,12,12,0,12,0,0,0,30,30,0,30,0,0,0,31,31,0,0,31,0,0,31,31,21,0,30,31,0,31,21,17,0,30,1,30,0,21,17,0,30,1,30,0,8,17,0,30,1,30,0,8,31,0,30,1,30,0,8,31,0,30,1,30,0,8,31,0,8,1,30,0,8,31,0,8,31,30,0,8,31,0,8,31,0,0,8,31,0,8,31,0,29,8,31,0,8,31,0,29,21,31,0,8,31,0,29,21,18,0,8,31,0,29,21,18,0,8,31,0,29,21,18,0,14,31,0,29,21,18,0,14,81,0,29,21,18,0,14,81,81,29,21,18,0,14,81,81,78,21,18,0,14,81,81,78,64,18,0,14,81,81,78,64,80,0,78,81,81,78,64,80,88,78,81,81,78,64,80,88,80,81,81,78,64,80,88,80,208,81,78,64,80,88,80,208,80,78,64,80,88,80,208,80,0,32,48,56,48,48,48,112,32,16,24,16,16,16,16,48,16,12,8,8,8,8,8,8,24,8,8,8,0,0,8,8,8,8,8,0,0,0,0,8,8,8,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0],"currentFrame":33,"length":34,"frames":34},"modifiedAt":"2022-10-27T22:22:57.166Z"}
# editor.blinkenrocket.de/?s=eyJkZWxheSI6MCwicmVwZWF0IjowLCJkaXJlY3Rpb24iOjAsImlkIjoiNTM5MTc5ZWUtNGFkNi00MDE0LTllMjAtNmFlYTRlYTEwOWZlIiwibmFtZSI6IiIsInNwZWVkIjo5LCJjcmVhdGlvbkRhdGUiOjE2NjY5MDgwMTYsInR5cGUiOiJwaXhlbCIsImFuaW1hdGlvbiI6eyJkYXRhIjpbMCwwLDAsMCwwLDgsMCwwLDAsMCwwLDAsMTIsMTIsMCwxMiwwLDAsMCwzMCwzMCwwLDMwLDAsMCwwLDMxLDMxLDAsMCwzMSwwLDAsMzEsMzEsMjEsMCwzMCwzMSwwLDMxLDIxLDE3LDAsMzAsMSwzMCwwLDIxLDE3LDAsMzAsMSwzMCwwLDgsMTcsMCwzMCwxLDMwLDAsOCwzMSwwLDMwLDEsMzAsMCw4LDMxLDAsMzAsMSwzMCwwLDgsMzEsMCw4LDEsMzAsMCw4LDMxLDAsOCwzMSwzMCwwLDgsMzEsMCw4LDMxLDAsMCw4LDMxLDAsOCwzMSwwLDI5LDgsMzEsMCw4LDMxLDAsMjksMjEsMzEsMCw4LDMxLDAsMjksMjEsMTgsMCw4LDMxLDAsMjksMjEsMTgsMCw4LDMxLDAsMjksMjEsMTgsMCwxNCwzMSwwLDI5LDIxLDE4LDAsMTQsODEsMCwyOSwyMSwxOCwwLDE0LDgxLDgxLDI5LDIxLDE4LDAsMTQsODEsODEsNzgsMjEsMTgsMCwxNCw4MSw4MSw3OCw2NCwxOCwwLDE0LDgxLDgxLDc4LDY0LDgwLDAsNzgsODEsODEsNzgsNjQsODAsODgsNzgsODEsODEsNzgsNjQsODAsODgsODAsODEsODEsNzgsNjQsODAsODgsODAsMjA4LDgxLDc4LDY0LDgwLDg4LDgwLDIwOCw4MCw3OCw2NCw4MCw4OCw4MCwyMDgsODAsMCwzMiw0OCw1Niw0OCw0OCw0OCwxMTIsMzIsMTYsMjQsMTYsMTYsMTYsMTYsNDgsMTYsMTIsOCw4LDgsOCw4LDgsMjQsOCw4LDgsMCwwLDgsOCw4LDgsOCwwLDAsMCwwLDgsOCw4LDAsMCwwLDAsMCwwLDgsMCwwLDAsMCwwLDAsMCwwXSwiY3VycmVudEZyYW1lIjozMywibGVuZ3RoIjozNCwiZnJhbWVzIjozNH0sIm1vZGlmaWVkQXQiOiIyMDIyLTEwLTI3VDIyOjIyOjU3LjE2NloifQo%3D
# 
# 
# https://github.com/blinkenrocket/firmware/blob/master/src/storage.cc
# i2c_read(uint8_t addrhi, uint8_t addrlo, uint8_t len, uint8_t *data)
# load(uint8_t idx, uint8_t *data)
#   - i2c_read(0, 1 + idx, 1, &page_offset);
#   - i2c_read(1 + (page_offset / 8), (page_offset % 8) * 32, 132, data);
#   -->
#   - page_offset = eeprom[1+idx]
#   - page_address = 256 + 32*page_offset
#   - page = eeprom[page_address .. page_address+132-1]
# loadChunk(uint8_t chunk, uint8_t *data)
#   - uint8_t this_page_offset = page_offset + (4 * chunk);
#   - i2c_read(1 + (this_page_offset / 8), (this_page_offset % 8) * 32 + 4, 128, data);
#   -->
#   - this_page_offset = page_offset + (4 * chunk)
#   - address = 256 + 32*this_page_offset + 4   # +4 to skip header
#   - data = eeprom[address .. address+128-1]
# eeprom[0] = num_anims
# 
# https://github.com/blinkenrocket/firmware/blob/master/src/display.h
# 
# https://eblot.github.io/pyftdi/api/i2c.html
# - ADBUS0: SCL, with pullup
# - ADBUS1, ADBUS2: both connected to SDA, with pullup

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
            print("DEBUG: %r" % payload)
            print("DEBUG: %r" % bytes(payload))
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

a = Animation.from_url("editor.blinkenrocket.de/?s=eyJkZWxheSI6MCwicmVwZWF0IjowLCJkaXJlY3Rpb24iOjAsIm5hbWUiOiIiLCJzcGVlZCI6OSwidHlwZSI6InBpeGVsIiwiYW5pbWF0aW9uIjp7ImRhdGEiOlswLDAsMCwwLDAsOCwwLDAsMCwwLDAsMCwxMiwxMiwwLDEyLDAsMCwwLDMwLDMwLDAsMzAsMCwwLDAsMzEsMzEsMCwwLDMxLDAsMCwzMSwzMSwyMSwwLDMwLDMxLDAsMzEsMjEsMTcsMCwzMCwxLDMwLDAsMjEsMTcsMCwzMCwxLDMwLDAsOCwxNywwLDMwLDEsMzAsMCw4LDMxLDAsMzAsMSwzMCwwLDgsMzEsMCwzMCwxLDMwLDAsOCwzMSwwLDgsMSwzMCwwLDgsMzEsMCw4LDMxLDMwLDAsOCwzMSwwLDgsMzEsMCwwLDgsMzEsMCw4LDMxLDAsMjksOCwzMSwwLDgsMzEsMCwyOSwyMSwzMSwwLDgsMzEsMCwyOSwyMSwxOCwwLDgsMzEsMCwyOSwyMSwxOCwwLDgsMzEsMCwyOSwyMSwxOCwwLDE0LDMxLDAsMjksMjEsMTgsMCwxNCw4MSwwLDI5LDIxLDE4LDAsMTQsODEsODEsMjksMjEsMTgsMCwxNCw4MSw4MSw3OCwyMSwxOCwwLDE0LDgxLDgxLDc4LDY0LDE4LDAsMTQsODEsODEsNzgsNjQsODAsMCwxNCw4MSw4MSw3OCw2NCw4MCw4OCwxNCw4MSw4MSw3OCw2NCw4MCw4OCw4MCw4MSw4MSw3OCw2NCw4MCw4OCw4MCwyMDgsODEsNzgsNjQsODAsODgsODAsMjA4LDgwLDc4LDY0LDgwLDg4LDgwLDIwOCw4MCwwLDMyLDQ4LDU2LDQ4LDQ4LDQ4LDExMiwzMiwxNiwyNCwxNiwxNiwxNiwxNiw0OCwxNiwxMiw4LDgsOCw4LDgsOCwyNCw4LDgsOCwwLDAsOCw4LDgsOCw4LDAsMCwwLDAsOCw4LDgsMCwwLDAsMCwwLDAsOCwwLDAsMCwwLDAsMCwwLDBdLCJjdXJyZW50RnJhbWUiOjIzLCJsZW5ndGgiOjM0LCJmcmFtZXMiOjM0fSwiaWQiOiJlODFjMTRlNi00NjllLTRkOTctYmVjZi1hMDA5YzE5NGI1YTciLCJtb2RpZmllZEF0IjoiMjAyMi0xMC0yOFQwMDoyODoxNS45MzlaIn0%3D")
a.repeat = 1
print(repr(a))

b = Animation.from_url("editor.blinkenrocket.de/?s=eyJkZWxheSI6MCwicmVwZWF0IjowLCJkaXJlY3Rpb24iOjAsImlkIjoiMGU2MzQ2MWQtNTVhZC00MzM3LWIwYmUtZjdlMDYzYThmM2FjIiwibmFtZSI6IiIsInNwZWVkIjoxMywiY3JlYXRpb25EYXRlIjoxNjY2OTA5NjQyLCJ0eXBlIjoidGV4dCIsInRleHQiOiIgIEpldHp0IGthbm5zdCBkdSBuaWNodCBtZWhyIGJlaGF1cHRlbiwgZGFzcyBkdSBuaWNodCBsb2V0ZW4ga2FubnN0IiwiYW5pbWF0aW9uIjp7ImRhdGEiOlswLDAsMCwwLDAsMCwwLDBdLCJjdXJyZW50RnJhbWUiOjAsImZyYW1lcyI6MSwibGVuZ3RoIjoxfSwibW9kaWZpZWRBdCI6IjIwMjItMTAtMjdUMjI6Mjc6MjQuMzkwWiJ9")
b.repeat = 1
print(repr(b))

c = Animation.from_url("editor.blinkenrocket.de/?s=eyJkZWxheSI6MS41LCJyZXBlYXQiOjAsImRpcmVjdGlvbiI6MCwiaWQiOiIxNDkwODA3Ni04M2M3LTQyYjAtOWI4Zi1lZTViNjVlMjhhZjciLCJuYW1lIjoiIiwic3BlZWQiOjUsImNyZWF0aW9uRGF0ZSI6MTY2NjkwOTY0OSwidHlwZSI6InBpeGVsIiwiYW5pbWF0aW9uIjp7ImRhdGEiOlswLDE5NiwxOTQsMTgsMTgsMTk0LDE5NiwwLDAsNjgsNjYsMTgsMTgsMTk0LDE5NiwwLDAsMTk2LDE5NCwxOCwxOCwxOTQsMTk2LDBdLCJjdXJyZW50RnJhbWUiOjIsImxlbmd0aCI6MywiZnJhbWVzIjozfSwibW9kaWZpZWRBdCI6IjIwMjItMTAtMjhUMDA6NDQ6MTEuMDQ0WiJ9")
c.repeat = 1
c = PixelAnimation(
	# 0
	" XX  XX " + "\n" +
	" XX  XX " + "\n" +
	"        " + "\n" +
	"   XX   " + "\n" +
	"        " + "\n" +
	" X    X " + "\n" +
	"  XXXX  " + "\n" +
	"        " + "\n",
	# 1
	"     XX " + "\n" +
	" XX  XX " + "\n" +
	"        " + "\n" +
	"   XX   " + "\n" +
	"        " + "\n" +
	" X    X " + "\n" +
	"  XXXX  " + "\n" +
	"        " + "\n",
	# 2
	" XX  XX " + "\n" +
	" XX  XX " + "\n" +
	"        " + "\n" +
	"   XX   " + "\n" +
	"        " + "\n" +
	" X    X " + "\n" +
	"  XXXX  " + "\n" +
	"        " + "\n",
	speed=5, delay=3, repeat=1)
print(repr(c))

#print(a.to_url())
#a.play()

eeprom_bytes = Animation.to_eeprom(a, b, c)
print(repr(eeprom_bytes))
abc2 = Animation.from_eeprom(eeprom_bytes)
print(abc2)
if repr([a, b, c]) != repr(abc2):
    print("not equal!")
    print("%r\n\n!=\n\n%r" % (repr([a, b, c]), repr(abc2)))

# https://github.com/blinkenrocket/firmware/blob/master/src/static_patterns.h
shutdownPattern = Animation.from_bytes(bytes([
	0x20, 0x40,
	0x0e, 0x0f,
	0xff, 0x81, 0x81, 0x81, 0x81, 0x81, 0x81, 0xff,
	0x7e, 0x42, 0x42, 0x42, 0x42, 0x42, 0x42, 0x7e,
	0x3c, 0x24, 0x24, 0x24, 0x24, 0x24, 0x24, 0x3c,
	0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18,
	0x00, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x00,
	0x00, 0x00, 0x18, 0x18, 0x18, 0x18, 0x00, 0x00,
	0x00, 0x00, 0x00, 0x18, 0x18, 0x00, 0x00, 0x00,
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
]))
#print(shutdownPattern)

turnonPattern = Animation.from_bytes(bytes([
    0x20, 0x40,
    0x0e, 0x0f,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,        
    0x00, 0x00, 0x00, 0x18, 0x18, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x18, 0x18, 0x18, 0x18, 0x00, 0x00,
    0x00, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x00,
    0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18, 0x18,
    0x3c, 0x24, 0x24, 0x24, 0x24, 0x24, 0x24, 0x3c,
    0x7e, 0x42, 0x42, 0x42, 0x42, 0x42, 0x42, 0x7e,
    0xff, 0x81, 0x81, 0x81, 0x81, 0x81, 0x81, 0xff
]))
#print(turnonPattern)

if True:
    print(eeprom_bytes)
    prom = I2cEEPROM("ftdi://ftdi:232h/1")
    print(prom.read_eeprom())
    prom.write_eeprom(eeprom_bytes)
