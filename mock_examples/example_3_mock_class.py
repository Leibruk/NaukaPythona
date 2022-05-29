import time
import random


class DataSet:

    def __init__(self):
        self.data = None

    def load_data(self):
        time.sleep(random.randint(0, 15))
        self.data = "DATA"

