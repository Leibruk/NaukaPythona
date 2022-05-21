test = "Moduł A zaimportowany."

def find(arr, el):
    for index, value in enumerate(arr):
        print(value)
        elindex = arr.index(el)
        if value == el:
            return f"Dany element ({el}) znajduje się w tablicy pod indeksem {elindex}"
    return f"Dany element ({el}) nie znajduje się w tablicy"

arr = [1, 2, 3, 4, 5]

print(find(arr, 3))