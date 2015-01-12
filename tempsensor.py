# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

class TempSensor(object):
    def __init__(self, gpio_temp):
        self.__gpio_temp = gpio_temp
        GPIO.setup(self.__gpio_temp, GPIO.IN)