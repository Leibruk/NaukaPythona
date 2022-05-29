import mock_examples
from mock_examples.example_1_mock_constant import neutral_celsius_to_fahrenheit


def test_example_1_no_mock_constant():
    expected = 68
    result = neutral_celsius_to_fahrenheit()
    assert expected == result


def test_example_1_mock_constant_50_expected(mocker):
    expected = 50
    mocker.patch.object(mock_examples.example_1_mock_constant, "NEUTRAL_TEMPERATURE", 10)
    result = neutral_celsius_to_fahrenheit()
    assert result == expected


def test_example_1_mock_constant_86_90_expected(mocker):
    expected = 86.90
    mocker.patch.object(mock_examples.example_1_mock_constant, "NEUTRAL_TEMPERATURE", 30.5)
    result = neutral_celsius_to_fahrenheit()
    assert result == expected
