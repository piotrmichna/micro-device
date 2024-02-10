import json

def write_file(filename, dat):
    """
    SAVE DEVICE CONFIGURATION TO FILE [*.cfg]

        Parameters:
            filename (str): name of file to save configuration json data
            dat (dict): python dictionary with data.

        Returns:
            (bool): result writing file.
    """
    if filename and dat and isinstance(dat, (dict,list)):
        dat = json.dumps(dat, separators=(',', ':'))
        with open(filename, 'w') as f:
            f.write(dat)
        return True
    return False
