import pytest


@pytest.fixture()
def start_database():
    print()
    print("Start Database...")
    yield


@pytest.mark.usefixtures("start_database")
def test_only_start_database():
    print()
    print("Get Data")
    print("Check Data")
    assert True


@pytest.fixture()
def close_database():
    yield
    print()
    print("Database closed...")


@pytest.mark.usefixtures("close_database")
def test_only_close_database():
    print()
    print("Get Data")
    print("Check Data")
    assert True


@pytest.fixture()
def start_close_database():
    print()
    print("Start Database...")
    yield
    print()
    print("Close database...")


@pytest.mark.usefixtures("start_close_database")
def test_start_close_database():
    print()
    print("Get data")
    print("Check data")
    assert True


@pytest.fixture()
def get_connection():
    print()
    print("Start Database...")
    print("Populat Database")
    yield "connection"
    print()
    print("Close database...")


@pytest.mark.usefixtures("get_connection")
def test_check_database_query(get_connection):
    print()
    connection = get_connection
    print(f"Wysyłam zapytanie do bazy danych za pomocą {connection}")
    print(connection.split("n"))
    assert True


@pytest.fixture()
def get_list():
    return [1, 2, 3, 4, 5, 8]


def test_check_reverse_list(get_list):
    result = sorted(get_list, reverse=True)
    expected_result = [8, 5, 4, 3, 2, 1]
    assert result == expected_result
