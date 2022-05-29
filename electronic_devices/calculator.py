from typing import Union

class NoBatteryError(ValueError):
    pass


class Calculator:
    def __init__(self, memory: int = 0, battery: int = 100 ):
        self.memory = memory
        self.battery = battery
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