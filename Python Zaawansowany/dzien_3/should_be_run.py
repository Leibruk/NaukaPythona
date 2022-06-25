
from typing import Callable

SHOULD_BE_RUN = True

def should_be_run(func: Callable) -> Callable:

    def wrapper(*args, **kwargs):
        if SHOULD_BE_RUN is True:
            x = func(*args, **kwargs)
            return x
        else:
            print("Pomijam...")
    return wrapper


@should_be_run
def hello():
    print("Hello world!")

run = should_be_run(hello)()
run