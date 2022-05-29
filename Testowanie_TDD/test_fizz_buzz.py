import pytest
from fizz_buzz.f_b import get_fizz_buzz


def test_check_fizz_buzz_return_1_when_1_given():
    # given
    test_value = 1
    expected = "1"
    # when
    result = get_fizz_buzz(test_value)
    # then
    assert result == expected


def test_check_fizz_buzz_return_2_when_2_given():
    # given
    test_value = 2
    expected = "2"
    # when
    result = get_fizz_buzz(test_value)
    # then
    assert result == expected


def test_check_fizz_buzz_return_Fizz_when_3_given():
    # given
    test_value = 3
    expected = "Fizz"
    # when
    result = get_fizz_buzz(test_value)
    # then
    assert result == expected


def test_check_fizz_buzz_return_Buzz_when_5_given():
    # given
    test_value = 5
    expected = "Buzz"
    # when
    result = get_fizz_buzz(test_value)
    # then
    assert result == expected


@pytest.mark.parametrize("test_value, expected", [(0, "0"), (1, "1"), (2, "2"), (4, "4"), (7, "7"), (8, "8")])
def test_check_fizz_buzz_return_int_to_str(test_value, expected):
    assert get_fizz_buzz(test_value) == expected


@pytest.mark.parametrize("test_value, expected", [(3, "Fizz"), (5, "Buzz"), (6, "Fizz"), (10, "Buzz"), (15, "FizzBuzz")])
def test_check_fizz_buzz_return_fizz_or_buzz_or_fizzbuzz(test_value, expected):
    assert get_fizz_buzz(test_value) == expected
