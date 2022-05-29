import time


def expensive_api_call():
    time.sleep(10)
    return 1000

def compute(x: int) -> int:
    response = expensive_api_call()
    return response + x
