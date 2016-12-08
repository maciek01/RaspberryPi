#!/usr/bin/python

import os
import time
import RPi.GPIO as GPIO

BZPIN = 11 #gpio 0

#GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD) 
GPIO.setwarnings(False)
GPIO.setup(BZPIN, GPIO.OUT)

current_milli_time = lambda: int(time.time() * 1000)

def beep(secs, period):

	global BZPIN

	start = current_milli_time()
	while current_milli_time() - start < secs * 1000:
		GPIO.output(BZPIN,GPIO.HIGH)
		time.sleep(period)
		GPIO.output(BZPIN,GPIO.LOW)
		time.sleep(period)


for i in range(0, 1):
	beep(1, 0.00005)
	time.sleep(1)
