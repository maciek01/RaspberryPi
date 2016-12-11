#!/usr/bin/python

import time, datetime as dt
import buzzer

HOURS = 10
MINUTES = 30

#HOURS = 0
#MINUTES = 23

while True:
	if dt.datetime.today().hour == HOURS and dt.datetime.today().minute == MINUTES:
		buzzer.alarm(60)
	else:
		time.sleep(10)



