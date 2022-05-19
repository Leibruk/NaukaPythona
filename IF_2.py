BLACK_LIST = ["Krzysiek"]

imie = input('Podaj imię: ')

if imie in BLACK_LIST:
    print("...")
else:
    print("Cześć " + imie)
