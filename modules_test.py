import pytest
from modules import Module
from params import Param

@pytest.fixture(scope='module')
def modul():
    dat = {
        "mid": 0, "chip_id": '', "typ": "BME280", "typ_id": 0,
        "params": [
            {
                "pid": 1, "name": "H1-bme", "dir_out": False, "sync_s": 5,
                "uid": 1, "uname": "Wilgotność", "uform_str": "ddd",
                "utyp_id": 1, "utyp_name": "Liczba całkowita", "utyp": "int"
            },
            {
                "pid": 2, "name": "T1-bme", "dir_out": False, "sync_s": 5,
                "uid": 2, "uname": "Temperatura", "uform_str": "fff.f",
                "utyp_id": 2, "utyp_name": "Zmiennoprzecinkowa",  "utyp": "float"
            }
        ]
    }
    return Module(data=dat)

def test_module_initialization(modul):
    assert isinstance(modul, Module)

@pytest.mark.parametrize('dir_out, utyp',(
        (False, 'str'),
        (False, 'int'),
        (True, 'bool'),
        (True, 'int'),
))
def test_module_update(modul, dir_out, utyp):
    assert len(modul._params) == 2
    dat = {
        "mid": 1, "chip_id": '', "typ": "BME280", "typ_id": 0, 'sync_s':2,
        "params": [
            {
                "pid": 1, "name": "H1-bme", "dir_out": False, "sync_s": 5,
                "uid": 1, "uname": "Wilgotność", "uform_str": "ddd",
                "utyp_id": 1, "utyp_name": "Liczba całkowita", "utyp": "int"
            },
            {
                "pid": 2, "name": "T1-bme", "dir_out": dir_out, "sync_s": 5,
                "uid": 2, "uname": "Temperatura", "uform_str": "fff.f",
                "utyp_id": 2, "utyp_name": "Zmiennoprzecinkowa",  "utyp": utyp
            }
        ]
    }
    modul.m_dict = dat
    assert modul._sync_s == 5
    assert modul.mid == 1
    assert modul.chip_id == ''
    assert modul.typ == 'BME280'
    assert modul.typ_id == 0
    p1 = modul._params[0]
    assert isinstance(p1, Param)
    assert p1.pid == 1
    assert p1.uid == 1
    assert p1.name == 'H1-bme'
    assert p1.dir_out == False

    assert modul.is_new == False



def test_module_remove_param(modul):
    assert len(modul._params) == 2
    dat = {
        "mid": 1, "chip_id": '0xae23', "typ": "BME280", "typ_id": 0,
        "params": [
            {
                "pid": 0, "name": "H1-bme"
            },
            {
                "pid": 2, "name": "T1-bme2", "dir_out": False, "sync_s": 5,
                "uid": 2, "uname": "Temperatura", "uform_str": "fff.f",
                "utyp_id": 2, "utyp_name": "Zmiennoprzecinkowa",  "utyp": "float"
            }
        ]
    }
    modul.m_dict = dat
    assert len(modul._params) == 1
    p1 = modul._params[0]
    assert isinstance(p1, Param)
    assert p1.name == 'T1-bme2'

def test_module_add_param(modul):
    dat = {
        "mid": 1, "chip_id": '', "typ": "BME280", "typ_id": 1,
        "params": [
            {
                "pid": 3, "name": "H1-bme", "dir_out": False, "sync_s": 5,
                "uid": 3, "uname": "Temperatura", "uform_str": "fff.f",
                "utyp_id": 3, "utyp_name": "Zmiennoprzecinkowa",  "utyp": "float"
            }
        ]
    }

    modul.m_dict = dat
    assert modul.typ_id == 1
    assert len(modul._params) == 2
    p1 = modul._params[1]
    assert isinstance(p1, Param)
    assert p1.name == 'H1-bme'

def test_module_change(modul):
    dat = {
        "mid": 1, "chip_id": '', "typ": "BME280", "typ_id": 1,
        "params": [
            {
                "pid": 3, "name": "H1-bme", "dir_out": False, "sync_s": 15,
                "uid": 3, "uname": "Temperatura", "uform_str": "fff.f",
                "utyp_id": 3, "utyp_name": "Zmiennoprzecinkowa",  "utyp": "float"
            }
        ]
    }
    modul.m_dict = dat
    assert modul.typ_id == 1
    assert len(modul._params) == 2
    p1 = modul._params[1]
    assert isinstance(p1, Param)
    assert p1.name == 'H1-bme'
    assert p1._sync_s == 15

    assert modul.is_changed == True
    dat = modul.m_dict
    assert modul.is_changed == False
    assert dat.get('mid') == 1

def test_module_add_param_val(modul):
    p1= modul._params[1]
    p1.set_val(vl=23.12)
    assert modul.is_new == True
