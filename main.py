# -*- coding: utf-8 -*-

#import RPi.GPIO as GPIO
#import time
#import sys
from robot import *
#from sensor import *
from led import *

#Merkliste Verwendung GPIO
GPIO_Pins = {
    "led1" : 1,
    "led2" : 1,
    "trigger" : 1,
    "echo" : 1,
    "dht11" : 1,
    "motor1_pin1" : 17,
    "motor1_pin2" : 18,
    "motor2_pin1" : 22,
    "motor2_pin2" : 23,
    }

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
