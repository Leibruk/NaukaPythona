
lista = [1, 2, 3, 4, 5]

def find(arr, el):
    if el in arr:
        index = arr.index(el)
        return f"Element ({el}) znajduje sie w liście pod indeksem {index}"
    else:
        return "Element nie znajduje się w liście"

print(find(lista, 3))