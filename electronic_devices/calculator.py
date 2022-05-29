import os
from typing import Union

class NoBatteryError(ValueError):
    pass


class NoFileDefinedError(FileNotFoundError):
    pass


class Calculator:
    def __init__(self, memory: int = 0, battery: int = 100, file = None ):
        self.memory = memory
        self.battery = battery
        self.file = file
        self.check_battery()

    def check_battery(self):
        if self.battery <= 0:
            raise NoBatteryError("No battery!")

    def add(self,*args) -> Union[int, float]:
        self.check_battery()
        result = 0
        for n in args:
            result += n
        self.battery -= 1
        self.memory = result
        return result

    def subtract(self,*args) -> Union[int, float]:
        self.check_battery()
        result = args[0]
        for n in args[1:]:
            result -= n
        self.battery -= 1
        self.memory = result
        return result

    def divide(self,*args) -> Union[int, float]:
        self.check_battery()
        result = args[0]
        for n in args[1:]:
            if n == 0:
                raise ValueError("Pamiętaj cholero nie dziel przez zero!")
            result /= n
        self.battery -= 1
        self.memory = result
        return result

    def nth_power(self, number: Union[int, float], power: Union[int, float]):
        self.check_battery()
        result = number ** power
        self.battery -= 1
        self.memory = result
        return result

    def _get_data(self):
        if not self.file:
            raise NoFileDefinedError("Nie zdefiniowałeś pliku!")
        if os.path.isfile(self.file):
            with open(self.file) as f:
                lines = f.readlines()
            lines_splited = [line.split(",") for line in lines]
            data = []
            for line in lines_splited:
                data.append([int(x) for x in line])
            return data
        return None

    def avg_from_file(self):
        self.check_battery()
        # https://realpython.com/python-walrus-operator/
        if not (data := self._get_data()):
            raise FileNotFoundError("Podana ściężka nie prowadzi do pliku!")
        result = [sum(x) / len(x) for x in data]
        self.battery -= 1
        self.memory = result
        return result