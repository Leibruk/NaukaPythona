import collections


def is_palindrome(text: str) -> bool:
    text_lower = text.lower()
    return text_lower == text_lower[::-1]


def is_isogram(text: str) -> bool:
    text_lower = text.lower()
    if len(text) <= 1:
        return True
    for i in text_lower:
        if text_lower.count(i) > 1:
            return False
    return True


def find_children(dancing_brigade):
    d = {letter: 0 for letter in dancing_brigade if letter.isupper()}
    for letter in dancing_brigade:
        if letter.islower():
            d[letter.upper()] += 1

    od = collections.OrderedDict(sorted(d.items()))

    return "".join([key + key.lower() * value for key, value in od.items()])

