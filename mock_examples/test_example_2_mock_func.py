from mock_examples.example_2_mock_func import compute


def test_example_2_no_mock():
    expected = 1001
    result = compute(1)
    assert result == expected


def test_example_2_mock(mocker):
    mocker.patch("mock_examples.example_2_mock_func.expensive_api_call", return_value=100)
    expected = 101
    result = compute(1)
    assert result == expected
