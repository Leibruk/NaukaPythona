from mock_examples.example_3_mock_class_main import init_data


def test_example_3_mock_class(mocker):
    expected = "OTHER DATA"
    mock_dataset = mocker.patch("mock_examples.example_3_mock_class_main.DataSet.load_data", return_value="OTHER DATA")
    result = init_data()
    assert result == expected
    mock_dataset.assert_called_once()