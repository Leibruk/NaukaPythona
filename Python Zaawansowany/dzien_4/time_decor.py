"""
    Dekorator obliczający czas działania funkcji
"""

import time


def measure_time(func):

    def timer(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Funkcja wywolywała się {end-start} sekund.")
        return result
    return timer



@measure_time
def long_hello_world():
    time.sleep(2)
    print("Hello World")

def add(a, b):
    return a+b

print(add.__name__)

#long_hello_world()