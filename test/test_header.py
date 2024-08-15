import pytest
import canonicaljson

from pybov import errors
from pybov.marketdata import header


def test_header_validation_ok():
    h = header.HeaderData('00', 'COTAHIST.2003', 'BOVESPA', '20040531')

    assert h.reg_type == '00'
    assert h.fname == 'COTAHIST.2003'
    assert h.source_type == 'BOVESPA'
    assert h.date == '20040531'


@pytest.mark.parametrize(
    'params,errcode,errdata',
    [
        (('99', 'COTAHIST.2003', 'BOVESPA', '20040531'), 1, {'reg_type': 'expected "00" but got "99"'}),
        (('00', 'COTAHIST. 2003', 'BOVESPA', '20040531'), 1, {'fname': 'Invalid fname format: "COTAHIST. 2003"'}),
        (('00', 'COTAHIST.2003', 'BOVESP', '20040531'), 1, {'source_type': 'Expected "BOVESPA" but got: "BOVESP"'}),
        (('00', 'COTAHIST.2003', 'BOVESPA', '2004531'), 1, {'fname': 'Invalid date format: "2004531"'})
    ]
)
def test_header_validation_reg_error(params, errcode, errdata):
    with pytest.raises(errors.PybovValidationError) as e:
        header.HeaderData(*params)
 
    assert e.value.message == 'Validation error'
    assert e.value.code == errcode
    assert e.value.data == errdata


def test_header_new_ok():
    hd = header.HeaderData('00', 'COTAHIST.2003', 'BOVESPA', '20040531')
    h = header.Header(hd)

    assert h.data == hd


@pytest.mark.parametrize(
    'params,errcode,errdata',
    [
        (('99', 'COTAHIST.2003', 'BOVESPA', '20040531'), 1, {'reg_type': 'expected "00" but got "99"'}),
        (('00', 'COTAHIST. 2003', 'BOVESPA', '20040531'), 1, {'fname': 'Invalid fname format: "COTAHIST. 2003"'}),
        (('00', 'COTAHIST.2003', 'BOVESP', '20040531'), 1, {'source_type': 'Expected "BOVESPA" but got: "BOVESP"'}),
        (('00', 'COTAHIST.2003', 'BOVESPA', '2004531'), 1, {'fname': 'Invalid date format: "2004531"'})
    ]
)
def test_header_new_error(params, errcode, errdata):
    with pytest.raises(errors.PybovValidationError) as e:
        header.Header(header.HeaderData(*params))
 
    assert e.value.message == 'Validation error'
    assert e.value.code == errcode
    assert e.value.data == errdata


def test_header_from_b3str_ok(b3data):
    h = header.Header.from_b3str(b3data[0])
    expected = header.HeaderData('00', 'COTAHIST.2003', 'BOVESPA', '20040531')

    assert h.data == expected


def test_header_from_b3str_err(b3data):
    with pytest.raises(errors.PybovValidationError):
        header.Header.from_b3str('009u0jido')


def test_header_to_b3str_ok(b3data):
    h = header.Header(header.HeaderData('00', 'COTAHIST.2003', 'BOVESPA', '20040531'))

    assert h.to_b3str() == b3data[0]


def test_to_json_ok():
    h = header.Header(header.HeaderData('00', 'COTAHIST.2003', 'BOVESPA', '20040531'))
    jsonstr = h.to_json()
    expected_jsonstr = canonicaljson.encode_canonical_json({
        'reg_type': '00',
        'fname': 'COTAHIST.2003',
        'source_type': 'BOVESPA',
        'date': '20040531'
    }).decode()

    for i in range(10):
        assert jsonstr == expected_jsonstr


def test_from_json_ok():
    h = header.Header.from_json(canonicaljson.encode_canonical_json({
        'reg_type': '00',
        'fname': 'COTAHIST.2003',
        'source_type': 'BOVESPA',
        'date': '20040531'
    }).decode())
    expected = header.HeaderData('00', 'COTAHIST.2003', 'BOVESPA', '20040531')

    assert h.data == expected


def test_from_json_decode_err():
    with pytest.raises(errors.PybovValidationError) as err:
        header.Header.from_json('{"regtype')

    assert err.value.code == 1
    assert err.value.data == {'_jsondata': 'Invalid json string: "{"regtype"'}


def test_from_json_validation_err():
    with pytest.raises(errors.PybovValidationError) as err:
        header.Header.from_json(canonicaljson.encode_canonical_json({
            'reg_type': '99',
            'fname': 'COTAHIST.2003',
            'source_type': 'BOVESPA',
            'date': '20040531'
        }).decode())

    assert err.value.code == 1
    assert err.value.data == {'reg_type': 'expected "00" but got "99"'}
