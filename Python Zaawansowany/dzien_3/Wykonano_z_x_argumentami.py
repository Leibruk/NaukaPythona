from typing import Callable


def dekorator(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print(args, kwargs)
        x = func(*args, **kwargs)
        print(f"Wykonano z {len(args + len(kwargs))} argumentami")
        return x

    return wrapper


@dekorator
def add(a, b):
    return a + b


print(add(a=5, b=15))
