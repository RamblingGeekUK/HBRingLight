import RPi.GPIO as gpio
import time

# Set Mode
gpio.setmode(gpio.BCM)

# Set Pin 18 as Output and Turn off // Turn OFF RGBW ring
# Setting the PIN low isn't switching off the LED

gpio.setup(18, gpio.OUT)
gpio.output(18, gpio.LOW)

gpio.setup(23, gpio.OUT)
gpio.output(23, gpio.LOW)
# gpio.output(23, gpio.HIGH)

gpio.setup(24, gpio.OUT)
gpio.output(24, gpio.LOW)
#gpio.output(24, gpio.HIGH)

