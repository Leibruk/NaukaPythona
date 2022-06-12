"""
    Przyklad dzialania klas abstrakcyjnych w Pythonie
"""

import abc


class MusicalInstrument(abc.ABC):

    @abc.abstractmethod
    def play(self):
        print("Nie wiem jak grać..")


class Drums(MusicalInstrument):

    def play_sound(self):
        print("Badumntssss")

    def play(self):
        print("Badumntssss11111111")

class Guitar(MusicalInstrument):

    def play_fine_sound(self):
        print("Brzdek")

    def play(self):
        print("Brzdek1111111")


drums = Drums()
drums.play()

guitar = Guitar()
guitar.play()

