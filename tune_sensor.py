import RPi.GPIO as GPIO
from time import time, sleep
from math import floor
import csv

def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(15, GPIO.OUT)
	GPIO.setup(21, GPIO.IN)

def getReading():
	GPIO.output(15, GPIO.HIGH)
	sleep(.05)
	read = GPIO.input(21)
	GPIO.output(15, GPIO.LOW)
	return read

def run():
	setup()
	interval = 10
	while(True):
		seconds = floor(time())
		if (seconds % interval == 0):
			reading = getReading()
			print(reading, seconds)
			with open('data1.csv', 'a') as log:
				writer = csv.writer(log, dialect='excel')
				writer.writerow([reading, seconds])
			sleep(1.5)
	
	GPIO.cleanup()

run()
