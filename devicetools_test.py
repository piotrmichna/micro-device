import pytest
from devicetools import int_format, float_format, read_file, remove_file, write_file


@pytest.mark.parametrize("val, frmt, result", (
    (None, 'gdd', None),
    (True, 'gdd', 1),
    (False, 'gdd', 0),
    ('False', 'gdd', 0),
    ('false', 'gdd', 0),
    ('f', 'gdd', 0),
    ('True', 'gdd', 1),
    (1111, 'd', 1),
    (1111, 'dd', 11),
    (1111, 'ddd', 111),
    (-1, 'ddd', 1),
    ("-12", '', -12),
    (-111, '', -111),
    (12.2, 'd', 2),
    (123.2, 'dd', 23),
    (1234.2, 'ddd', 234),
    (-1.2, 'ddd', 1),
    (-12.2, 'gddd', -12),
    (-1234.3, 'gddd', -234),
))
def test_int_format(val, frmt, result):
    result_num = int_format(sval=val, frm=frmt)
    assert result_num == result


@pytest.mark.parametrize("val, frmt, result", (
    (None, 'gff.ff', None),
    (True, 'gff.f', None),
    (False, 'gff.f', None),
    ('False', 'gff.f', None),
    ('false', 'gff.f', None),
    ('f', 'gff.f', None),
    ('True', 'gff.f', None),
    (123.12, 'gff.f', 23.1),
    (-123, 'ff.ff', 23.0),
    (123.2, 'gfff.f', 123.2),
    ('g-1', 'ff', None),
    (-1, 'ff', 1.0),
    (-12, 'gff.f', -12.0),
    (-123.4, 'gfff.f', -123.4),
    (12.2, 'f.f', 2.2),
    ('-123.2', '', -123.20),
    ('1234.2C', 'gff.f', 34.2),
    (-1.2, 'gff.ff', -1.20),
    (-12.2, 'ff.ff', 12.20),
    (-1234.3, 'f.ff', 4.30),
))
def test_float_format(val, frmt, result):
    result_num = float_format(sval=val, frm=frmt)
    assert result_num == result


@pytest.mark.parametrize('file, data, expected', (
    ('dupa.xc', None, None),
    ('dupa.xc', {'name': 'Adam'}, {'name': 'Adam'}),
    ('', {'name': 'Adam'}, None),
    (None, {'name': 'Adam'}, None),
))
def test_read_file(file, data, expected):
    write_file(file, dat=data)
    response = read_file(file)
    assert response == expected
    remove_file(filename=file)
    response = read_file(file)
    assert response == None


@pytest.mark.parametrize('file', ('dupa.xc', '', None,))
def test_read_none_file(file):
    response = read_file(file)
    assert response == None
