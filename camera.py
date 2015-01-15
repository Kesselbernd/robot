# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
from picamera import *

GPIO.setmode(GPIO.BCM)

class CAMERA(PiCamera):
    def __init__(self):

    def foto(self):
        self.resolution = (1024, 768)
        self.start_preview()
        # Camera warm-up time
        time.sleep(2)
        zeit = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        self.capture('bild_' + zeit + '.jpg')

    def stream(self):
        pass

#Install on PI python-picamera python3-picamera python-picamera-docs
#http://www.raspberrypi.org/learning/python-picamera-setup/
#http://picamera.readthedocs.org/en/release-1.9/recipes1.html

