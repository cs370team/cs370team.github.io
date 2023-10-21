from random import random

class Sensor:
    def __init__(self, _, __):
        self.value = 1
    
    def reading(self):
        self.value = (self.value + int(random() / 0.9)) % 2
        return self.value