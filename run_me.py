# Sample script for HC-SR04 ultrasonic sensor
# Tested on Orange Pi Pc Plus v1.1
# How to run this script:
# sudo python run_me.py

from pyA20.gpio import gpio
from pyA20.gpio import port
import time

TRIG = port.PA21
ECHO = port.PC3

gpio.init()

print "Distance Measurement In Progress"

gpio.setcfg(TRIG, gpio.OUTPUT)
gpio.setcfg(ECHO, gpio.INPUT)

gpio.output(TRIG, 0)

print "Waiting For Sensor To Settle"

time.sleep(2)
gpio.output(TRIG, 1)
time.sleep(0.00001)
gpio.output(TRIG, 0)

while gpio.input(ECHO) == 0:
    pulse_start = time.time()

while gpio.input(ECHO) == 1:
    pulse_end = time.time()

pulse_duration = pulse_end - pulse_start

distance = pulse_duration * 17150

distance = round(distance, 2)

print("Distance: " + str(distance) + "cm")
