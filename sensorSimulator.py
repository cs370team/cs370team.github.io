from random import random

class Sensor:

    low_value = 1

    def __init__(self, v1, v2):
        self.value = 1
        self.low = v1==15
    
    def reading(self):
        self.value = (self.value + int(random() / 0.6)) % 2
        if self.low:
            Sensor.low_value = self.value
        else:
            self.value = max(self.value, Sensor.low_value)
        return self.value
