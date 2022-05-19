BLACK_LIST = ["Radek", "Stefan", "Piotr", "Adam", "Andrzej"]

first_name = input("Podaj imię: ")

if first_name in BLACK_LIST:
    print("Jesteś już na BLACKLIST, Witaj " + first_name)
else:
    print(input("Chcesz się przywitać?" ))
    x = input()
        if input():
            print("Witaj" + first_name)
        else:
            BLACK_LIST.append(first_name)
            print("Witaj " + first_name + "Zostałeś dodany do BLACKLIST")





