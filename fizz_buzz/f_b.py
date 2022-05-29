def get_fizz_buzz(x: int) -> str:
    if x == 0:
        return str(x)
    if is_multiple(x,3):
        if is_multiple(x, 5):
            return "FizzBuzz"
        return "Fizz"
    if is_multiple(x, 5):
        return "Buzz"
    return str(x)


def is_multiple(value: int, mod: int) -> bool:
   return (value % mod == 0)