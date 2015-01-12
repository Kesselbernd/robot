# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)

class Sensor(object):
    def __init__(self, gpio_trigger, gpio_echo):
        #GPIO Pins zuweisen
        self.__GPIO_TRIGGER = gpio_trigger
        self.__GPIO_ECHO = gpio_echo

        #Richtung der GPIO-Pins festlegen (IN / OUT)
        GPIO.setup(self.__GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.__GPIO_ECHO, GPIO.IN)

    def distanz(self):
        # setze Trigger auf HIGH
        GPIO.output(self.getTriggerPin(), True)

        # setze Trigger nach 0.01ms aus LOW
        time.sleep(0.00001)
        GPIO.output(self.getTriggerPin(), False)

        StartZeit = time.time()
        StopZeit = time.time()

        # speichere Startzeit
        while GPIO.input(self.__GPIO_ECHO) == 0:
          StartZeit = time.time()

        # speichere Ankunftszeit
        while GPIO.input(self.__GPIO_ECHO) == 1:
          StopZeit = time.time()

        # Zeit Differenz zwischen Start und Ankunft
        TimeElapsed = StopZeit - StartZeit
        # mit der Schallgeschwindigkeit (34300 cm/s) multiplizieren
        # und durch 2 teilen, da hin und zurueck
        distanz = (TimeElapsed * 34300) / 2

        return distanz

    def getDistanceInMeters(self):
        return self.distanz()/100

    def getTriggerPin(self):
        return self.__GPIO_TRIGGER

    def getEchoPin(self):
        return self.__GPIO_ECHO