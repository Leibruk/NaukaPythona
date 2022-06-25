def get_nth(n: int) -> int:
    if n < 0:
        raise ValueError("Uważaj ciąg fibonacciego nie ma ujemnych elementów lub zmiennoprzecinkowych")
    fib = [0, 1]
    for _ in range(n):
        fib.append(fib[i] + fib[i + 1])
    return fib[n]


def fib_nth(n):
    a, b = 0, 1
    yield a
    for _ in range(n):
        a, b = b, a+b
        yield a


print(list(fib_nth(5)))

