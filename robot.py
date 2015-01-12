# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import random
from sensor import *
from led import *

GPIO.setmode(GPIO.BCM)

class Robot(object):
    def __init__(self, gpio_trigger, gpio_echo, sicherheitsabstand):
        self.sensor = Sensor(gpio_trigger, gpio_echo)
        self.__sicherheitsabstand = sicherheitsabstand
        self.blinker_links = LED(22)
        self.blinker_rechts = LED(17)

    def __lt__(self): #gibt True oder False zurück
        return self.sensor.distanz() < self.__sicherheitsabstand

    def fahren(self):
        if self.__lt__() == False:
            print("Ich fahre gerade aus!")
        else:
            self.lenken()

    def lenken(self):
        self.__richtung = random.randint(0, 1)
        while self.__lt__() == True:
            print("Ich muß meine Richtung ändern!")
            if self.__richtung == 0:
                print("Ich drehe nach rechts")
                self.blinken()
            if self.__richtung == 1:
                print("Ich drehe nach links")
                self.blinken()

    def blinken(self):
        if self.__richtung == 0:
            while self.__lt__() == True:
                self.blinker_rechts.blinken()

        if self.__richtung == 1:
            while self.__lt__() == True:
                self.blinker_links.blinken()