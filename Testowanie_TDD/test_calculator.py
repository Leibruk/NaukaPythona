import pytest
from electronic_devices.calculator import Calculator, NoBatteryError


def test_init_calculator():
    calc = Calculator()
    assert calc.memory == 0
    assert calc.battery == 100

def test_calculatpor_raise_no_battery_error():
    with pytest.raises(NoBatteryError):
        Calculator(memory=0, battery=0)

def test_calculator_add_two_numbers():
    calc = Calculator()
    expected = 4
    result = calc.add(2,2)
    assert result == expected
    assert calc.memory == result
    assert calc.battery == 99

def test_calculator_add_multiple_numbers():
    calc = Calculator()
    expected = 9
    result = calc.add(3, 3, 3)
    assert result == expected
    assert calc.memory == result
    assert calc.battery == 99