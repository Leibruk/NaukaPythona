"""
    obliczanie silni n! iteracyjnie
"""


def factorial(n):
    """Wylicza silnie z n.

    :param n: liczba natrualna
    :return: wyliczona silnia
    """
    result = 1

    for i in range(1, n + 1):
        result *= i
    return result


print(factorial(4))


