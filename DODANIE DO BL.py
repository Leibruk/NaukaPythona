black_list = {"Damian", "Marek", "Darek", "Andrzej"}

while True:
    first_name = input("Podaj imie, na którym chcesz operować: ")
    action = input("Co chcesz zrobić? (D)odać albo (P)rzywitać się: ")
    if (action == "D"):
        black_list.add(first_name)
    elif (action == "P"):
        if first_name in black_list:
            print("Nie witam się z Toba!")
        else:
            print(f"Hello {first_name}!")
    else:
        print("Nie rozumiem polecenia")
    print("Finisz")
