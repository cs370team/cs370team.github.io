from sensor import Sensor
from time import time, sleep
from math import floor
import csv

interval = 5

def run():
	sensor1 = Sensor(15, 21)
	sensor2 = Sensor(2, 27)
	
	while (True):
		seconds = floor(time())
		if (seconds % interval == 0):
			reading = [seconds, sensor1.reading(), sensor2.reading()]
			print(reading)
			with open('data.csv', 'a') as log:
				writer = csv.writer(log, dialect='excel')
				writer.writerow(reading)
			sleep(1.5)

run()
