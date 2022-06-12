import abc


class Animals(abc.ABC):

    def __init__(self, name: str):
        self.name = name

    @abc.abstractmethod
    def make_noise(self):
        ...

    @abc.abstractmethod
    def move(self):
        ...

    @abc.abstractmethod
    def eat(self):
        ...

class Dog(Animals):

    def __init__(self, name: str, ferocity: int):
        super().__init__(name)
        self.ferocity = ferocity

    def make_noise(self):
        print("Hau Hau!")

    def move(self):
        print("4, 4, 4, 4")

    def eat(self):
        print("Jem kość.")


class Fish(Animals):

    def __init__(self, name: str, swim_speed: float):
        super().__init__(name)
        self.swim_speed = swim_speed

    def make_noise(self):
        print("Bul bul bul")

    def move(self):
        print("~~~~~~~~~~")

    def eat(self):
        print("Jem robaczki.")


class Bird(Animals):

    def __init__(self, name: str, flight_speed: float):
        super().__init__(name)
        self.flight_speed = flight_speed

    def make_noise(self):
        print("Cwir Cwir")

    def move(self):
        print("^^^^^^^^")

    def eat(self):
        print("Jem ziarna.")

class Zoo:

    def __init__(self, animals):
        self.animals = animals

    def open_zoo(self):
        for animal in self.animals:
            animal.move()
            animal.make_noise()

    def close_zoo(self):
        for animal in self.animals:
            animal.eat()
            animal.make_noise()
            animal.move()

# animals = [Dog("Burek",100), Fish("Nemo",50), Bird("Ara", 13)]

zoo_wroclaw = Zoo([Dog("Burek",100), Fish("Nemo",50), Bird("Ara", 13)])
zoo_wroclaw.open_zoo()
zoo_wroclaw.close_zoo()

