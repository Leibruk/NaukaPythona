from mock_examples.example_4_mock_delete_file import remove_file


def test_example_4_mock_delete_file(mocker):
    mocker.patch("mock_examples.example_4_mock_delete_file.os.path.exists", return_value=True)
    mock_remove = mocker.patch("mock_examples.example_4_mock_delete_file.os.remove")
    remove_file("cokolwiek")
    mock_remove.assert_called_once_with("cokolwiek")
    mock_remove.assert_called_once()
