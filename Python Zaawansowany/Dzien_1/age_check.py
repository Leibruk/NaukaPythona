"""
    sprawdzenie wieku użytkownika na podstawie inputu
"""

age = int(input("Podaj swoj wiek: "))

if age < 18:
    print("Użytkownik niepełnoletni.")
    print(f"Do uzyskania pełnoletności pozostało {18 - age} lat.")
elif age >= 18 and age < 100:
    print("Użytkownik pełnoletni.")
else:
    print("200 lat!!!")

