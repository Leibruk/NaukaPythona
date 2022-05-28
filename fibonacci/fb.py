def get_nth(n: int) -> int:
    if n < 0:
        raise ValueError("Uważaj ciąg fibonacciego nie ma ujemnych elementów")
    fib = [0, 1]
    for i in range(n):
        fib.append(fib[i] + fib[i + 1])
    return fib[n]
