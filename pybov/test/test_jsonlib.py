import pytest

from pybov import errors, jsonlib


def test_encode_ok():
    data = {'a': 1}

    assert jsonlib.encode(data) == '{"a":1}'


def test_encode_err():
    data = {'a': object()}
    with pytest.raises(errors.PybovValidationError) as err:
        jsonlib.encode(data)

    assert err.value.code == 1
    assert err.value.data == {'_jsondata': f'Data type cannot be converted to json: "{data}"'}


def test_decode_ok():
    data = '{"a": 1}'

    assert jsonlib.decode(data) == {'a': 1}


def test_decode_err():
    with pytest.raises(errors.PybovValidationError) as err:
        jsonlib.decode('{"a: 1}')

    assert err.value.code == 1
    assert err.value.data == {'_jsondata': 'Invalid json string: "{"a: 1}"'}
