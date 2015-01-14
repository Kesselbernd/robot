# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class rtk(object):
    def __init__(self, gpio_pin1, gpio_pin2):
        self.__GPIO_PIN1 = gpio_pin1
        self.__GPIO_PIN2 = gpio_pin2
        GPIO.setup(self.__GPIO_PIN1, GPIO.OUT)
        GPIO.setup(self.__GPIO_PIN2, GPIO.OUT)

    def vorwaerts(self):
        GPIO.output(self.__GPIO_PIN1, 0)
        time.sleep(1)
        GPIO.output(self.__GPIO_PIN2, 1)
        time.sleep(5)

    def rueckwaerts(self):
        GPIO.output(self.__GPIO_PIN2, 0)
        time.sleep(1)
        GPIO.output(self.__GPIO_PIN1, 1)
        time.sleep(5)


"""
##Simple motor script for the RTK-000-001
import RPi.GPIO as GPIO
import time
#Set to broadcom pin numbers
GPIO.setmode(GPIO.BCM)

#Motor 1 = Pins 17 and 18
#Motor 2 = Pins 22 and 23
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

#Now loop forever turning one direction for 5 seconds, then the other
while (True):
    #Sleep 1 second then turn 17 on
    GPIO.output(18, 0)
    time.sleep(1)
    GPIO.output(17, 1);
    time.sleep(5);
    #And now the other way round
    GPIO.output(17, 0)
    time.sleep(1);
    GPIO.output(18, 1);
    time.sleep(5);
    #And loop back around
    #And final cleanup
GPIO.cleanup()
"""