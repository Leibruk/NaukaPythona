

class StrArgTypeError(Exception):
    pass


class NumberArgTypeError(Exception):
    pass


class BoolArgTypeError(Exception):
    pass


class LenGreaterThanOneError(Exception):
    pass


def check_type(text):
    if type(text) is str:
        raise StrArgTypeError

    if type(text) is int:
        raise NumberArgTypeError

    if type(text) is bool:
        raise BoolArgTypeError

    if text is None:
        print("None jest okej")

    if type(text) in (list, dict, set, tuple) and len(text) > 1:
        raise LenGreaterThanOneError

if __name__ == "__main__":

    try:
        check_type(7)
    except StrArgTypeError:
        print("Błąd STR")
    except NumberArgTypeError:
        print("Błąd NUM")
    except BoolArgTypeError:
        print("Błąd BOOL")
    except LenGreaterThanOneError:
        print("Błąd LEN")
    finally:
        print("Koniec funkcji")

