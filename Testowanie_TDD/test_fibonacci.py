import pytest
from fibonacci.fb import get_nth


def test_should_return_13_when_7_given():
    # given
    test_value = 7
    expected_value = 13
    # when
    result = get_nth(test_value)
    # then
    assert result == expected_value


def test_schould_raise_value_error_when_negative():
    with pytest.raises(ValueError):
        get_nth(-10)


@pytest.mark.parametrize("test_value, expected_result", [(1, 1), (7, 13), (16, 987), (100, 354224848179261915075)])
def test_check_nth_fibonacci(test_value, expected_result):
    assert get_nth(test_value) == expected_result
