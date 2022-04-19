import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(23, gpio.OUT)

gpio.output(23, gpio.LOW)
time.sleep(4)
gpio.output(23, gpio.HIGH)

gpio.setup(24, gpio.OUT)

gpio.output(24, gpio.LOW)
time.sleep(4)
gpio.output(24, gpio.HIGH)
