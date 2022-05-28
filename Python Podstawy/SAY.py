class Person:
    def __init__(self, who, voice_stamina):
        self.who = who
        self._voice_stamina = voice_stamina

    def say(self, what):
        if self._voice_stamina == 0:
            print("Nie masz już głosu!")
        else:
            print(what)
            self._voice_stamina = max (0, self._voice_stamina - 20)
            print(self._voice_stamina)

    def sing(self, what):
        if self._voice_stamina == 0:
            print("Nie masz już głosu!")
        else:
            print(what.upper())
            self._voice_stamina = max (0, self._voice_stamina - 60)
            print(self._voice_stamina)

    def maybe_eat(self, new_stamina):
        if self._voice_stamina == 0:
            self._voice_stamina += new_stamina
            self.voice_stamina = self.voice_stamina + new_stamina
            print(self._voice_stamina)
        else:
            print("Stamina wystarczająca")

    @property
    def voice_stamina(self):
        print("voice stamina getter!")
        return self._voice_stamina

    @voice_stamina.setter
    def voice_stamina(self, new_stamina):
        print("voice stamina setter!")
        if new_stamina < 0 or new_stamina > 100:
            raise ValueError("wrong stamina; 0 to 100 is allowed")
        self._voice_stamina = new_stamina


person_1=Person("Radek", 0)
person_2=Person("Zbyszek", 100)

if __name__ == '__main__':
    person_1.say('Jestem Piękny')
    person_2.say("Hello World!")
    person_2.sing("Hello World!")
    person_2.sing("Hello World!")
    person_2.voice_stamina = 100
    print(person_2.voice_stamina)
    person_2.sing("Hello World!")
    person_2.sing("Hello World!")
    person_2.sing("Hello World!")
    person_2.maybe_eat(50)
    person_2.sing("Hello World!")
    person_2.sing("Hello World!")


