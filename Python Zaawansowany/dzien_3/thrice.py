from typing import Callable


def thrice(func: Callable) -> Callable:

    def wrapper(*args, **kwargs):
        for _ in range(3):
            x = func(*args, **kwargs)
        return x
    return wrapper

@thrice
def hello():
    print("Hello world!")

x = hello()

