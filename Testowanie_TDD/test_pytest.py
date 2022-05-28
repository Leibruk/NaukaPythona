import pytest


def test_passed():
    assert True


@pytest.mark.failed
def test_failed():
    assert False


@pytest.mark.skip(reason="Bo tak chcę")
def test_skipped():
    assert True


@pytest.mark.skipif(condition="sys.platform != 'win32'")
def test_skipped_if():
    assert True


@pytest.mark.tryfirst
def test_try_first():
    assert True
