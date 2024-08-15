import pytest

from pybov.errors import PybovError


def test_basic_ok():
    e = PybovError('foo')

    assert e.message == 'foo'
    assert e.code == 1
    assert str(e) == 'foo'
    assert repr(e) == '[1] foo'


def test_full_ok():
    e = PybovError('foo', 5)

    assert e.message == 'foo'
    assert e.code == 5
    assert str(e) == 'foo'
    assert repr(e) == '[5] foo'


def test_exception_ok():
    with pytest.raises(PybovError):
        raise PybovError('pytest')
