import pytest
from example.check_text import is_palindrome, is_isogram, find_children
from example.example_01 import delete_nth


@pytest.mark.parametrize("my_text, result",
                         [("asa", True), ("leibruk", False), ("KrKrk", False), ("!!!", True), ("2aA2", True)])
def test_is_palindrome(my_text, result):
    assert is_palindrome(my_text) is result


@pytest.mark.parametrize("my_text, result",
                         [("a", True), ("ab", True), ("ja chce", False), ("Aa", False), ("!@", True)])
def test_is_isogram(my_text, result):
    assert is_isogram(my_text) is result


@pytest.mark.parametrize("my_text, result",
                         [("aA", "Aa"), ("bBAa", "AaBb"), ("!aAbD", "AabD"), ("0aA", "Aa"), ("a A", "Aa")])
def test_find_children(my_text, result):
    assert find_children(my_text) == result


def test_check_delete_nth_when_2_give():
    # given
    foto_list = [1, 2, 3, 3, 4, 4, 5]
    # when
    duplication = 1
    # then
    assert delete_nth(foto_list, duplication) == [1, 2, 3, 4, 5]


def test_check_delete_nth_when_2_give():
    # given
    foto_list = ["a", 3, 3, "a", 4, 4, 5]
    # when
    duplication = 1
    # then
    assert delete_nth(foto_list, duplication) == ["a", 3, 4, 5]


def test_check_delete_nth_when_1_give():
    # given
    foto_list = ["a", 3, 3, "a", 4, "!", 1, 4, 5, 2, 3, 3]
    # when
    duplication = 1
    # then
    assert delete_nth(foto_list, duplication) == ["a", 3, 4, 5]

def test_check_delete_nth_when_3_give():
    # given
    foto_list = ["a", 3, 3, "a", 4, 4, 5, 4, "Tak", "Tak", -10, -10]
    # when
    duplication = 2
    # then
    assert delete_nth(foto_list, duplication) == ["a", 3, 3, "a", 4, 4, 5, "Tak", "Tak", -10, -10]
