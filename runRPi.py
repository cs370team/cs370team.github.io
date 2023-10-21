# from sensor import Sensor
from sensorSimulator import Sensor
from time import time, sleep
from math import floor
import csv
import os


interval = 60*5 #delay between sensor readings in seconds

def run():
	# sensor1 = Sensor(15, 21)
	# sensor2 = Sensor(2, 27)
	sensor1 = Sensor(15, 21)
	sensor2 = Sensor(2, 27)
	
	while (True):
		seconds = floor(time())
		if (seconds % interval == 0):
			reading = [seconds, sensor1.reading(), sensor2.reading()]
			with open('data.csv', 'a') as log:
				writer = csv.writer(log, dialect='excel')
				writer.writerow(reading)
			sleep(1.5)
			os.system("push.sh")

run()
