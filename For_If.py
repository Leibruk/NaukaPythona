
BLACK_LIST = ["Radek", "Stefan", "Piotr", "Adam", "Andrzej"]

for first_name in BLACK_LIST:
    print("nowa iteracja")
    if first_name == "Radek":
        print("Just before cotinue")
        continue
    print(first_name)