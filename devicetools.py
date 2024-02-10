import json
import os


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
