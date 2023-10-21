#on outside pin row

import RPi.GPIO as GPIO
from time import time, sleep
from math import floor
import csv

pins = [15, 21]

class Sensor:
	def __init__(self, power, sensor):
		self.power = power
		self.sensor = sensor
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.power, GPIO.OUT)
		GPIO.setup(self.sensor, GPIO.IN)

	def reading(self):
		GPIO.output(self.power, GPIO.HIGH)
		sleep(.05)
		reading = GPIO.input(self.sensor)
		GPIO.output(self.power, GPIO.LOW)
		return reading
