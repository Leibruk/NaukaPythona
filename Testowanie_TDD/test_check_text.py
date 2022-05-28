import pytest
from example.check_text import is_palindrome, is_isogram, find_children


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
