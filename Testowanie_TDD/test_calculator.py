import pytest
from electronic_devices.calculator import Calculator, NoBatteryError


def test_init_calculator():
    calc = Calculator()
    assert calc.memory == 0
    assert calc.battery == 100


def test_calculatpor_raise_no_battery_error():
    with pytest.raises(NoBatteryError):
        Calculator(memory=0, battery=0)


@pytest.mark.parametrize("test_values, expected", [((2, 2), 4), ((3, 3, 3), 9)])
def test_calculator_add_(test_values, expected):
    calc = Calculator()
    assert calc.add(*test_values) == expected
    assert calc.memory == expected
    assert calc.battery == 99

@pytest.mark.parametrize("test_values, expected", [((2, 2), 0), ((3, 3, 3), -3)])
def test_calculator_subtract_(test_values, expected):
    calc = Calculator()
    assert calc.subtract(*test_values) == expected
    assert calc.memory == expected
    assert calc.battery == 99