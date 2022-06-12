"""
    Nalezy zdefiniowa klase String
"""


class String():

    def __init__(self, text):
        self.text = text

    def __add__(self, obj):
        return len(self.text) + len(obj.text)

    def __eq__(self, obj):
        return len(self.text) == len(obj.text)


str1 = String("Abc")
str2 = String("Xyz")
print(str1 + str2)
print(str1 == str2)
