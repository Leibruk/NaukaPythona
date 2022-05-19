class Animal:
    def __init__(self, name="Rex", age=2):
        self.__name = name
        self.__age = age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be grater than 0.")

    def get_age(self):
        return self.__age


my_dog = Animal()
my_dog.set_age(3)
print(my_dog.get_age())