


from typing import Union

def podaj_imie(imie: str) -> Union[str,int]:
    if type(imie) is str:
        print(f"Podaj imię: {imie}")
        return imie
    else:
        print("Błedny typ arg imie!!!")
        return -1

x = podaj_imie(23)
print(x)