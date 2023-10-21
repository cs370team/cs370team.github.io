#on inside pin row

import RPi.GPIO as GPIO
from time import time, sleep
from math import floor
import csv

def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(2, GPIO.OUT)
	GPIO.setup(27, GPIO.IN)

def getReading():
	GPIO.output(2, GPIO.HIGH)
	sleep(.05)
	read = GPIO.input(27)
	GPIO.output(2, GPIO.LOW)
	return read
