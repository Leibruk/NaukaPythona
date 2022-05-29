from mock_examples.example_5_mock_create_directory import create_dir


def test_check_create_dir(mocker):
    mock_mkdir = mocker.patch("mock_examples.example_5_mock_create_directory.os.mkdir")
    result = create_dir("cokolwiek")
    assert result == 201
    mock_mkdir.assert_called_once_with("cokolwiek")

def test_check_create_dir_failed(mocker):
    mock_mkdir = mocker.patch("mock_examples.example_5_mock_create_directory.os.mkdir", side_effect=OSError)
    result = create_dir("cokolwiek")
    assert result == 500
    mock_mkdir.assert_called_once_with("cokolwiek")