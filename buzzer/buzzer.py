#!/usr/bin/python

import time, datetime as dt
import RPi.GPIO as GPIO


HOURS = 10
MINUTES = 30

#HOURS = 0
#MINUTES = 23

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




def alarm(secs):
	for i in range(0, secs * 2):
		beep(0.3, 0.00005)
		time.sleep(0.2)




while True:
	if dt.datetime.today().hour == HOURS and dt.datetime.today().minute == MINUTES:
		alarm(60)



