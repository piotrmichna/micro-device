import pytest
from params import Param


@pytest.fixture
def param():
    dat = {"pid": 1, "name": "T1-bme", "dir_out": False, "sync_s": 5, "uid": 2, "uname": "Temperatura",
           "uform_str": "fff.f", "utyp_id": 3, "utyp_name": "Zmiennoprzecinkowa", "utyp": "float"}

    return Param(data=dat)


def test_param_initialization(param):
    assert isinstance(param, Param)


@pytest.mark.parametrize("typ, expected", (
    ('str', 'str'),
    ('int', 'int'),
    ('float', 'float'),
    ('bool', 'bool'),
    (None, 'float'),
))
def test_param_utyp(param, typ, expected):
    param.p_dict = {'utyp': typ}
    assert param._utyp == expected


@pytest.mark.parametrize("stamp, dir_out, val, typ, frt, expected", (
    ('', False, 'Tekst', 'str', '', 'Tekst'),
    ('', False, 1, 'int', 'ddd', 1),
    ('', False, 1.3, 'int', 'ddd', 1),
    ('', False, 1.1, 'float', 'ff.f', 1.1),
    ('', False, 123.1, 'float', 'ff.f', 23.1),
    ('', False, 1.1, 'float', 'ff.ff', 1.10),
    ('', False, 1, 'bool', '', True),
    ('', False, 0.1, 'bool', '', True),
    ('', False, True, 'bool', '', True),
    ('', False, 'dupa', 'bool', '', True),
    ('', False, 'Fdupa', 'bool', '', False),
    ('', False, 0, 'bool', '', False),
    ('', False, False, 'bool', '', False),
    ('', False, None, 'float', '', None),
    # with stamp time
    ('20:04:01', False, 'Tekst', 'str', '',
     {'val': 'Tekst', 'stamp': '20:04:01'}),
    ('20:04:01', False, 1, 'int', 'ddd', {'val': 1, 'stamp': '20:04:01'}),
    ('20:04:01', False, 1.3, 'int', 'ddd', {'val': 1, 'stamp': '20:04:01'}),
    ('20:04:01', False, 1.1, 'float', 'ff.f',
     {'val': 1.1, 'stamp': '20:04:01'}),
    ('20:04:01', False, 123.1, 'float', 'ff.f',
     {'val': 23.1, 'stamp': '20:04:01'}),
    ('20:04:01', False, 1.1, 'float', 'ff.ff',
     {'val': 1.10, 'stamp': '20:04:01'}),
    ('20:04:01', False, 1, 'bool', '', {'val': True, 'stamp': '20:04:01'}),
    ('20:04:01', False, 0.1, 'bool', '', {'val': True, 'stamp': '20:04:01'}),
    ('20:04:01', False, True, 'bool', '', {'val': True, 'stamp': '20:04:01'}),
    ('20:04:01', False, 'dupa', 'bool', '',
     {'val': True, 'stamp': '20:04:01'}),
    ('20:04:01', False, 'Fdupa', 'bool', '',
     {'val': False, 'stamp': '20:04:01'}),
    ('20:04:01', False, 0, 'bool', '', {'val': False, 'stamp': '20:04:01'}),
    ('20:04:01', False, False, 'bool', '',
     {'val': False, 'stamp': '20:04:01'}),
    ('20:04:01', False, None, 'float', '', None),
    # with params for output IO
    ('20:04:01', True, 'Tekst', 'str', '', {'val': True, 'stamp': '20:04:01'}),
    ('20:04:01', True, 'False', 'str', '',
     {'val': False, 'stamp': '20:04:01'}),
    ('20:04:01', True, True, 'bool', '', {'val': True, 'stamp': '20:04:01'}),
    ('20:04:01', True, False, 'bool', '', {'val': False, 'stamp': '20:04:01'}),
    ('20:04:01', True, 1, 'int', '', {'val': True, 'stamp': '20:04:01'}),
    ('20:04:01', True, 0, 'int', '', {'val': False, 'stamp': '20:04:01'}),

))
def test_param_val_setter(param, stamp, dir_out, val, typ, frt, expected):
    param.p_dict = {'dir_out': dir_out, 'utyp': typ, "uform_str": frt}
    param.set_val(val, stamp=stamp)
    assert param.val == expected
