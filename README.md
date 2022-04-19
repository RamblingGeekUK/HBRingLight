# HBRingLight

Working to try and control a inexpensive Ring Light sourced form a UK Store, HomeBargin. 

### Hardware

The hardware has 3 strips of LED's 

Ring 1 : RGBW - These appear to be NeoPixels
Ring 2 : Cool White LED's
Ring 3 : Warm White LED's

Thier are 5 cables in total.

Black - Ground
Red - Power (5v)*
Yellow - Warm White LED's
White - RGBW/NeoPixels
Green - Cool White LED's

### RaspberryPi

You need to install the following NeoPixel Lib first before these will run. 

```sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel```

GPIO Pins for Referencec

![GPIO PINS](https://github.com/RamblingGeekUK/HBRingLight/images/pins.png)
