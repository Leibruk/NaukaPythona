"""
    Definicja dekoratora z wypisywaniem autora funkcji
"""

from typing import Callable


def hello():
    print("Hello world!")


# dekorator to funkcja
# dekorator musi przyjmosc inna funckje jako argument
# dekoratu musi definiowac funkcję wewnenętrzną

def author(func: Callable) -> Callable:
    def wrapper():
        print("Autor: JA!")
        func()

    return wrapper


# hello()
decorated_func = author(hello)
decorated_func()
