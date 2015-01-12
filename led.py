# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
#import random

GPIO.setmode(GPIO.BCM)

class LED(object):
    def __init__(self, gpio_led):
        self.__gpio_led = gpio_led
        GPIO.setup(self.__gpio_led, GPIO.OUT)

    def led_on(self):
        GPIO.output(self.__gpio_led, True)

    def led_off(self):
        GPIO.output(self.__gpio_led, False)

    def blinken(self):
        GPIO.output(self.__gpio_led, True)
        time.sleep(0.3)
        GPIO.output(self.__gpio_led, False)
        time.sleep(0.3)

    def getLedPin(self):
        return self.__gpio_led