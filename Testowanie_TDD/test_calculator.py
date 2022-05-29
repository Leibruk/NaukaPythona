import io

import pytest
from electronic_devices.calculator import Calculator, NoBatteryError


@pytest.fixture()
def calc():
    calc = Calculator()
    assert calc.memory == 0
    assert calc.battery == 100
    return calc


def test_calculatpor_raise_no_battery_error():
    with pytest.raises(NoBatteryError):
        Calculator(memory=0, battery=0)


@pytest.mark.parametrize("test_values, expected", [((2, 2), 4), ((3, 3, 3), 9)])
def test_calculator_add_(test_values, expected, calc):
    assert calc.add(*test_values) == expected
    assert calc.memory == expected
    assert calc.battery == 99


@pytest.mark.parametrize("test_values, expected", [((2, 2), 0), ((3, 3, 3), -3)])
def test_calculator_subtract_(test_values, expected, calc):
    assert calc.subtract(*test_values) == expected
    assert calc.memory == expected
    assert calc.battery == 99


def test_check_calculator_divide_raise_value_error(calc):
    with pytest.raises(ValueError):
        calc.divide(5, 0)


@pytest.mark.parametrize("test_number, test_power, expected", [(2, 2, 4), (10, 2, 100)])
def test_check_calculator_to_nth_power(test_number, test_power, expected, calc):
    assert calc.nth_power(test_number, test_power) == expected
    assert calc.memory == expected
    assert calc.battery == 99


def test_check_calculator_avg_from_file(mocker, calc):
    mock__get_data = mocker.patch("electronic_devices.calculator.Calculator._get_data",
                                  return_value=[[1, 2], [2, 2, 2], [1, 1, 1, 5, 2]])
    expected = [1.5, 2.0, 2.0]
    result = calc.avg_from_file()
    assert result == expected
    mock__get_data.assert_called_once()


def test_check_calculator__get_data(mocker, calc):
    fake_file = io.StringIO("1,2\n2,2,2\n1,1,1,5,2")
    mock_os = mocker.patch("electronic_devices.calculator.os")
    mock_open = mocker.patch("electronic_devices.calculator.open", return_value=fake_file)
    calc.file = "fake_file.txt"
    assert calc._get_data() == [[1, 2], [2, 2, 2], [1, 1, 1, 5, 2]]
    mock_open.asser_called_once_with("fake_file.txt")
    mock_os.path.isfile.assert_called_once_with("fake_file.txt")