import pytest

from pybov import helpers


@pytest.mark.parametrize(
    's,length,char,order',
    [
        ('foo', 30, ' ', 1),
        ('foo', 3, ' ', 1),
        ('foo', 5, ' ', -1),
        ('foo', 30, ' ', 30)
    ]
)
def test_fill_str_ok(s, length, char, order):
    filled = helpers.fill_str(s, length, char, order)
    if order == 1:
        expected = s + (char * (length - len(s)))
    else:
        expected = (char * (length - len(s))) + s 

    assert len(filled) == length
    assert filled == expected 
