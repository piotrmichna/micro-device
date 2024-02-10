import json
import os


def int_format(sval, frm):
    if not (isinstance(frm, str) and len(frm)):
        frm = 'gddd'
    sign = ''
    if isinstance(frm, str) and len(frm):
        if frm[0].lower() == 'g':
            sign = 'g'
            frm = frm[1:]

    if sval is None:
        return None
    else:
        if isinstance(sval, bool):
            sval = '1' if sval is True else '0'
        if sval == 'False':
            sval = '0'

        if not isinstance(sval, str):
            sval = str(sval)

        if '.' in sval:
            sval = str(sval).split('.')
            sval = sval[0]
        if sval:
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
            if len(sval) > len(frm):
                sval = sval[len(sval) - len(frm):]
            sval = sign + sval
            try:
                sval = int(sval)
            except ValueError:
                sval = None
            return sval
        return None


def float_format(sval, frm):
    if not (isinstance(frm, str) and len(frm) and ('.' in frm)):
        frm = 'gfff.ff'

    if sval is None:
        return None
    frm = frm.lower().replace('f', 'd')
    ar = frm.split('.')

    if not isinstance(sval, float):
        try:
            sval = float(sval)
        except ValueError:
            pass
    if isinstance(sval, float):
        sval = f'{sval:.{len(ar[1])}f}'

    sar = str(sval).split('.')
    d = int_format(sar[0], frm=ar[0])
    if len(sar) > 1:
        sval = f'{d}.{sar[1]}'
    else:
        sval = f'{d}.0'
    try:
        sval = float(sval)
    except ValueError:
        return None
    return sval


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
    try:
        os.remove(filename)
    except OSError:
        return False
    return True
