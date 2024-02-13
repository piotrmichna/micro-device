import json
import os


def int_format(sval, frm):
    if not (isinstance(frm, str) and len(frm)):
        frm = 'gddd'
    sign = ''
    print(f'sval:{sval}, frm:{frm}')
    if isinstance(frm, str) and len(frm):
        if frm[0].lower() == 'g':
            sign = 'g'
            frm = frm[1:]

    if sval is None:
        return None
    else:
        try:
            sval = int(sval)
        except ValueError:
            pass

        if isinstance(sval, str):
            if (sval == '') or (sval.lower()[0] == 'f'):
                sval = '0'
            else:
                sval = '1'

        if not isinstance(sval, str):
            sval = str(sval)

        if (sign == 'g') and (sval[0] == '-'):
            sign = '-'
            sval = sval[1:]
        else:
            sign = ''
        nb = ''
        for c in sval:
            if 47 < ord(c) < 58:
                nb += c
        sval = nb
        print(f'sval:{sval}')
        if len(sval) > len(frm):
            sval = sval[len(sval) - len(frm):]
        sval = sign + sval

        return int(sval)


def float_format(sval, frm):
    if not (isinstance(frm, str) and len(frm)):
        frm = 'gfff.ff'

    if sval in (None, False, True):
        return None
    if isinstance(sval, str):
        while len(sval) and not (47 < ord(sval[-1]) < 58):
            sval = sval[:-1]
        if len(sval) == 0:
            return None
        try:
            sval = float(sval)
        except ValueError:
            return None

    frm = frm.lower().replace('f', 'd')
    ar = frm.split('.')

    if not isinstance(sval, float):
        sval = float(sval)

    if isinstance(sval, float):
        if len(ar) > 1:
            sval = f'{sval:.{len(ar[1])}f}'

    sar = str(sval).split('.')
    # print(f'sval:{sval}, sar:{sar}, ar:{ar}')
    d = int_format(sar[0], frm=ar[0])
    print(f'd:{d}')
    if len(sar) > 1:
        sval = f'{d}.{sar[1]}'
    else:
        sval = f'{d}.0'

    return float(sval)


def write_file(filename, dat):
    """
    SAVE DEVICE CONFIGURATION TO FILE [*.cfg]

        Parameters:
            filename (str): name of file to save configuration json data
            dat (dict): python dictionary with data.

        Returns:
            (bool): result writing file.
    """
    if filename and dat and isinstance(dat, (dict, list)):
        dat = json.dumps(dat, separators=(',', ':'))
        with open(filename, 'w') as f:
            f.write(dat)
        return True
    return False


def read_file(filename):
    """
    READ DEVICE CONFIGURATION FROM FILE [*.cfg]

        Parameters:
            filename (str): name of file with configuration json data

        Returns:
            data (dict): python dictionary or None when data is't load.
    """
    if not filename:
        return None
    try:
        with open(filename, "r") as f:
            dat = f.read()
    except OSError:
        return None
    if dat:
        dat = json.loads(str(dat))
    return dat


def remove_file(filename):
    """
    REMOVE DEVICE CONFIGURATION FILE [*.cfg]

        Parameters:
            filename (str): name of configuration file to remove.

        Returns:
            (bool): result deleting file.
    """
    if not filename:
        return False
    try:
        os.remove(filename)
    except OSError:
        return False
    return True
