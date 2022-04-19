import RPi.GPIO as gpio
import time

# Set Mode
gpio.setmode(gpio.BCM)

# Set Pin 18 as Output and Turn off // Turn OFF RGBW ring
gpio.setup(18, gpio.OUT)
gpio.output(18, gpio.OFF)

gpio.setup(23, gpio.OUT)
gpio.output(23, gpio.OFF)
# gpio.output(23, gpio.HIGH)

gpio.setup(24, gpio.OUT)
gpio.output(24, gpio.OFF)
#gpio.output(24, gpio.HIGH)

