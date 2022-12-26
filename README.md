Generate animations for [blinkenrocket][blinkenrocket] with Python (instead of / in addition to using the [online editor][editor])
and program them into the EEPROM without using the MCU, i.e. you can do this before soldering. This can be used to make customized
blinkenrockets as a present.

Features:

- Create animations in Python, e.g. by "painting" with 'X' and space in a string (see `demo.py`).
- Import and export from/ to the [online editor][editor] (using URLs like [this][example_url]).
- Play animations in the terminal.
- Write animations to the EEPROM using an FT232H-based programmer.
- Write EEPROM data to a file and use another programmer, e.g. based on CH341A with a solder-free IC clamp.
- Non-feature: Download animations with the audio protocol. Instead, import them into the online editor or use [this script][audio_script].

I have tested this with the animations in `demo.py` on one blinkenrocket so there is a good chance that this will work on the first try
(it did for me, at least). Nonetheless, you should test it if you can. You may be using features that I haven't used/tested and there could
be an error in your scripts, e.g. I was setting the repeat count on the wrong animation.


Usage
=====

see `demo.py`


Hardware setup for FT232H
=========================

First, let me suggest that you use the usual, cheap EEPROM programmers instead of FT232H. They are available for $5 including shipping
and a solder-free clamp for SOIC8. `demo.py` will write the data to `eeprom.bin`.

I used the FT232H because I had given my EEPROM programmer to a friend and didn't have the time to get it back (or order another one).
The downside is that you have to solder two wires to the blinkenrocket unless you have the right clamp or some spare hands. In addition,
the FT232H is not ideal for I2C because it needs external pullups and SDA must be connected to two of its pins, i.e. you will have to
solder (or use a breadboard) even if you have a solder-free way to connect to the blinkenrocket.

The pinout is as follows ([source][pinout_source]):

- ADBUS0: SCL, with pullup
- ADBUS1, ADBUS2: both connected to SDA, with pullup
- VCC and GND: They are available on the pin headers. You can plug male jumper wires into the holes and apply some pressure with your finger.

Then, enable the code near the end of `demo.py` and run it.


[blinkenrocket]: http://blinkenrocket.de/
[editor]: http://editor.blinkenrocket.de/
[audio_script]: https://github.com/blinkenrocket/firmware/blob/master/utilities/blinkenrocket.py
[example_url]: http://editor.blinkenrocket.de/?s=eyJkZWxheSI6MCwicmVwZWF0IjowLCJkaXJlY3Rpb24iOjAsIm5hbWUiOiIiLCJzcGVlZCI6OSwidHlwZSI6InBpeGVsIiwiYW5pbWF0aW9uIjp7ImRhdGEiOlswLDAsMCwwLDAsOCwwLDAsMCwwLDAsMCwxMiwxMiwwLDEyLDAsMCwwLDMwLDMwLDAsMzAsMCwwLDAsMzEsMzEsMCwwLDMxLDAsMCwzMSwzMSwyMSwwLDMwLDMxLDAsMzEsMjEsMTcsMCwzMCwxLDMwLDAsMjEsMTcsMCwzMCwxLDMwLDAsOCwxNywwLDMwLDEsMzAsMCw4LDMxLDAsMzAsMSwzMCwwLDgsMzEsMCwzMCwxLDMwLDAsOCwzMSwwLDgsMSwzMCwwLDgsMzEsMCw4LDMxLDMwLDAsOCwzMSwwLDgsMzEsMCwwLDgsMzEsMCw4LDMxLDAsMjksOCwzMSwwLDgsMzEsMCwyOSwyMSwzMSwwLDgsMzEsMCwyOSwyMSwxOCwwLDgsMzEsMCwyOSwyMSwxOCwwLDgsMzEsMCwyOSwyMSwxOCwwLDE0LDMxLDAsMjksMjEsMTgsMCwxNCw4MSwwLDI5LDIxLDE4LDAsMTQsODEsODEsMjksMjEsMTgsMCwxNCw4MSw4MSw3OCwyMSwxOCwwLDE0LDgxLDgxLDc4LDY0LDE4LDAsMTQsODEsODEsNzgsNjQsODAsMCwxNCw4MSw4MSw3OCw2NCw4MCw4OCwxNCw4MSw4MSw3OCw2NCw4MCw4OCw4MCw4MSw4MSw3OCw2NCw4MCw4OCw4MCwyMDgsODEsNzgsNjQsODAsODgsODAsMjA4LDgwLDc4LDY0LDgwLDg4LDgwLDIwOCw4MCwwLDMyLDQ4LDU2LDQ4LDQ4LDQ4LDExMiwzMiwxNiwyNCwxNiwxNiwxNiwxNiw0OCwxNiwxMiw4LDgsOCw4LDgsOCwyNCw4LDgsOCwwLDAsOCw4LDgsOCw4LDAsMCwwLDAsOCw4LDgsMCwwLDAsMCwwLDAsOCwwLDAsMCwwLDAsMCwwLDBdLCJjdXJyZW50RnJhbWUiOjIzLCJsZW5ndGgiOjM0LCJmcmFtZXMiOjM0fSwiaWQiOiJlODFjMTRlNi00NjllLTRkOTctYmVjZi1hMDA5YzE5NGI1YTciLCJtb2RpZmllZEF0IjoiMjAyMi0xMC0yOFQwMDoyODoxNS45MzlaIn0%3D
[pinout_source]: https://eblot.github.io/pyftdi/api/i2c.html
