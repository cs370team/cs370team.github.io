from format_index import update_html
# from sensorSimulator import Sensor
from notification import lawn_notification
from sensor import Sensor
from time import time, sleep
from math import floor
import csv
import os


interval = 60 #delay between sensor readings in seconds (demo time, every minute)

#interval = 28800 #delay between sensor readings in seconds (every 8 hours)
push_path = "/home/acyo/Desktop/Project/cs370team.github.io/push.sh"

def run():
	sensor1 = Sensor(15, 21)
	sensor2 = Sensor(2, 27)

	while (True):
		seconds = floor(time())
		if (seconds % interval == 0):
			reading = [seconds, sensor1.reading(), sensor2.reading()]
			with open('data.csv', 'a') as log:
				writer = csv.writer(log, dialect='excel')
				writer.writerow(reading)
			update_html()
			lawn_notification()
			#add full path if push.sh not found
			os.system(push_path) #This can't happen too frequently or we'll run into issues both with github and with readings getting lost
			sleep(1)


if (__name__ == "__main__"):
	run()
