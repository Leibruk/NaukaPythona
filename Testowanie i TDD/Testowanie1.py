def divide(fisrt: float, second: float) -> float:
    try:
        return fisrt / second
    except ZeroDivisionError:
        print("Nie wolno dzielic przez zero")


print(divide(8, 3))
print(divide(3, 0))


