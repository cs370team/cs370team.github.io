from sensor import Sensor
from time import sleep

interval = 1

def run():
	sensor1 = Sensor(15, 21)
	sensor2 = Sensor(2, 27)
	
	while (True):
		reading = f"{sensor1.reading()}, {sensor2.reading()}"
		print(reading)
		sleep(interval)

run()
