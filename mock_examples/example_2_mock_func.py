import time
import random



def expensive_api_call():
    time.sleep(10)
    return random.randint(0, 1000)

def compute(x: int) -> int:
    response = expensive_api_call()
    return response + x
