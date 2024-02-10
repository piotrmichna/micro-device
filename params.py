class Param:

    def __init__(self, dat: dict = {}):
        self._pid = 0
        self._name = ''
        self._dir_out = None
        self._sync_s = 0
        self._uid = 0
        self._uname = ''
        self._uform_str = ''
        self._utyp = ''
        self._utpy_name = ''
        self._utyp_id = 0
        self._val = None

    def set_dict(self, dat):
        flag = False
        if dat and isinstance(dat, dict):
            if isinstance(dat.get('pid'), int) and self._pid != dat['pid']:
                self._pid = dat['pid']
                flag = True
            if isinstance(dat.get('name'), str) and self._name != dat['name']:
                self._name = dat['name']
                flag = True
            if isinstance(dat.get('dir_out'), bool) and self._dir_out != dat['dir_out']:
                self._dir_out = dat['dir_out']
                flag = True
            if isinstance(dat.get('sync_s'), int) and self._sync_s != dat['sync_s']:
                self._sync_s = dat['sync_s']
                flag = True
            if isinstance(dat.get('uid'), int) and self._uid != dat['uid']:
                self._uid = dat['uid']
                flag = True
            if isinstance(dat.get('uname'), str) and self._uname != dat['uname']:
                self._uname = dat['uname']
                flag = True
            if isinstance(dat.get('uform_str'), str) and self._uform_str != dat['uform_str']:
                self._uform_str = dat['uform_str']
                flag = True
            if isinstance(dat.get('utyp'), str) and self._utyp != dat['utyp']:
                self._utyp = dat['utyp']
                flag = True
            if isinstance(dat.get('utpy_name'), str) and self._utpy_name != dat['utpy_name']:
                self._utpy_name = dat['utpy_name']
                flag = True
            if isinstance(dat.get('utyp_id'), int) and self._utyp_id != dat['utyp_id']:
                self._utyp_id = dat['utyp_id']
                flag = True
            if self._dir_out is True and isinstance(dat.get('val'), bool):
                if self._val != dat['val']:
                    self.val = dat['val']
                    flag = True
        return flag
