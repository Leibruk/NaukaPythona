def get_nth(n: int) -> int:
    if n < 0:
        raise ValueError("Uważaj ciąg fibonacciego nie ma ujemnych elementów lub zmiennoprzecinkowych")
    fib = [0, 1]
    for i in range(n):
        fib.append(fib[i] + fib[i + 1])
    return fib[n]

if __name__ == '__main__':
    while True:
        print("Sprawdź n-ty wyraz ciągu fibonacciego")
        n = input("Podaj n: ")
        try:
            result = get_nth(int(n))
            print(result)
        except (ValueError, TypeError) as e:
            print(e)
            print("Spróbuj jeszcze raz")