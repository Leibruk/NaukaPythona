def sumator(*args, **kwargs):
    result = 0
    for arg in args:
        result = result + arg
    for key in kwargs:
       result = result + kwargs[key]
    return result

if __name__ == "__main__":
    print(f"Nie " + str(sumator(1, 2, 3, spam=42)))
    print(f"takie " + str(sumator(1, 2, 3, 4, cheese=10)))
    print(f"proste xD " + str(sumator(a=1, b=2, c=3, d=4, e=10)))
    