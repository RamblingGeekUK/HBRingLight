# HBRingLight

Working to try and control a inexpensive Ring Light sourced form a UK Store, HomeBargin. 

### Hardware

The hardware has 3 strips of LED's 

Ring 1 : RGBW - These appear to be NeoPixels
Ring 2 : Cool White LED's
Ring 3 : Warm White LED's

Thier are 5 cables in total.

Cable Colour | Function
Black - Ground
Red - Power (5v)*
Yellow - Warm White LED's
White - RGBW/NeoPixels
Green - Cool White LED's

### RaspberryPi

You need to install the following NeoPixel Lib first before these will run. 

```sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel```

GPIO Pins for Reference

![GPIO PINS](https://github.com/RamblingGeekUK/HBRingLight/blob/main/images/pins.png)

Green  RGBW       18
White  White Cool 23
Yellow White Warm 24

![IRL GPIO PINS](https://github.com/RamblingGeekUK/HBRingLight/blob/main/images/irlpins.png)


The pixel.py has been configured with the above GPIO's Pins, run it with SUDO.

```sudo python pixel.py```