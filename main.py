# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import sys
from robot import *
from sensor import *
from led import *

try:
    while True:
        #Robot(gpio_trigger, gpio_echo, sicherheitsabstand)
        robot = Robot(18, 24, 13)

        time.sleep(0.5)

        output = "Gemessene Entfernung = %05.1f cm (%.2f m)" % (robot.sensor.distanz(), robot.sensor.getDistanceInMeters())
        print(output)

        robot.fahren()
        time.sleep(0.5)

# Beim Abbruch durch STRG+C resetten
except KeyboardInterrupt:
    print("Fahrt vom User gestoppt")
    GPIO.cleanup()
