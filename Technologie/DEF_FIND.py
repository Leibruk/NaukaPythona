test = "To jest nowa wiadomość z modułu DEF_FIND"

def find(arr, el):
    if el in arr:
        index = arr.index(el)
        return f"Element ({el}) znajduje sie w liście pod indeksem {index}"
    else:
        return "Element nie znajduje się w liście"

