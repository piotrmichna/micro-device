from devicetools import float_format, int_format
# from time import ticks_add, ticks_diff, ticks_ms


class Param:
    def __init__(self, data: dict = {}):
        self._pid = 0
        self._name = ''
        self._dir_out = False
        self._sync_s = 0
        self._ticks_ms = 0
        self._uid = 0
        self._uname = ''
        self._uform_str = ''
        self._utyp = ''
        self._utpy_name = ''
        self._utyp_id = 0
        self._val = []
        self._changed = False
        if data and isinstance(data, dict):
            self.p_dict = data

    @property
    def name(self):
        return self._name

    @property
    def pid(self):
        return self._pid

    @property
    def uid(self):
        return self._uid

    @property
    def dir_out(self):
        return self._dir_out

    @property
    def is_changed(self):
        return self._changed

    # def _ticks_add(self):
    #     if self._sync_s > 0:
    #         if (self._ticks_ms == 0) or (ticks_diff(self._ticks_ms, ticks_ms()) < 0):
    #             self._ticks_ms = ticks_add(ticks_ms(), self._sync_s*1000)
    #             return True
    #     return False

    # @property
    # def is_ready(self):
    #     return self._ticks_add()

    @property
    def is_new(self):
        """CHECK IS NEW VALUES"""
        if len(self._val):
            return True
        return False

    @property
    def val_dict(self):
        """RETURN AND REMOW ALL IN LIST OF VALUES"""
        val = []
        while len(self._val):
            val.append(self._val.pop(0))
        if len(val):
            return {'pid': self._pid, 'vals': val}
        return None

    @property
    def val_pop(self):
        """RETURN AND REMOVE FIRST IN LIST OF VALUES"""
        if len(self._val):
            return self._val.pop(0)
        return None

    @property
    def val(self):
        """RETRUN FIRST IN LIST OF VALUES"""
        if len(self._val):
            return self._val[0]
        return None

    def set_val(self, vl, stamp: str = ''):
        """ADD VALUE TO LIST

        Params:
            vl (eny): value of param
            stamp (str): datetime stamp of measure, 
                if empty values list contain values else contain dict
        """
        if not isinstance(stamp, str):
            stamp = ''
        pars_vl = None

        if self._utyp and isinstance(self._utyp, str) and not (vl is None):
            if self._dir_out is False:
                if self._utyp == 'int':
                    pars_vl = int_format(sval=vl, frm=self._uform_str)
                    self._changed = True
                elif self._utyp == 'float' and isinstance(vl, (int, float)):
                    pars_vl = float_format(sval=vl, frm=self._uform_str)
                    self._changed = True
                elif self._utyp == 'bool':
                    if isinstance(vl, bool):
                        pars_vl = vl
                        self._changed = True
                    elif isinstance(vl, (int, float)):
                        pars_vl = bool(vl)
                        self._changed = True
                    elif isinstance(vl, str):
                        pars_vl = False if 'f' in vl.lower() else True
                        self._changed = True
                elif self._utyp == 'str':
                    if not vl is None:
                        pars_vl = str(vl)
            else:
                if isinstance(vl, str):
                    if 'f' in vl.lower():
                        pars_vl = False
                    else:
                        pars_vl = True
                else:
                    pars_vl = bool(vl)
        if pars_vl is not None:
            if len(stamp) > 7:
                pars_vl = {'val': pars_vl, 'stamp': stamp}
            if self._dir_out is False or (len(self._val) == 0):
                self._val.append(pars_vl)
            else:
                self._val[0] = pars_vl

    @property
    def p_dict(self):
        self._changed = False
        """DICT OF ALL CONFIGURED CLASS PARAMS"""
        dat = {'pid': self._pid, 'name': self._name, 'dir_out': self._dir_out,
               'sync_s': self._sync_s, 'uid': self._uid, 'uname': self._uname,
               'uform_str': self._uform_str, 'utyp': self._utyp,
               'utpy_name': self._utpy_name, 'utyp_id': self._utyp_id,
               'val': self._val[0] if len(self._val) else None}

        return dat

    @p_dict.setter
    def p_dict(self, dat):
        """SETTER BY DICT"""
        if dat and isinstance(dat, dict):
            if isinstance(dat.get('pid'), int) and self._pid != dat['pid']:
                self._pid = dat['pid']
                self._changed = True
            if isinstance(dat.get('name'), str) and self._name != dat['name']:
                self._name = dat['name']
                self._changed = True
            if isinstance(dat.get('dir_out'), bool) and self._dir_out != dat['dir_out']:
                self._dir_out = dat['dir_out']
                self._changed = True
            if isinstance(dat.get('sync_s'), int) and self._sync_s != dat['sync_s']:
                self._sync_s = dat['sync_s']
                # if self._sync_s > 0:
                #     self._ticks_add()
                # else:
                #     self._ticks_ms = 0
                self._changed = True
            if isinstance(dat.get('uid'), int) and self._uid != dat['uid']:
                self._uid = dat['uid']
                self._changed = True
            if isinstance(dat.get('uname'), str) and self._uname != dat['uname']:
                self._uname = dat['uname']
                self._changed = True
            if isinstance(dat.get('uform_str'), str) and self._uform_str != dat['uform_str']:
                self._uform_str = dat['uform_str']
                self._changed = True
            if isinstance(dat.get('utyp'), str) and self._utyp != dat['utyp']:
                self._utyp = dat['utyp']
                self._changed = True
            if isinstance(dat.get('utpy_name'), str) and self._utpy_name != dat['utpy_name']:
                self._utpy_name = dat['utpy_name']
                self._changed = True
            if isinstance(dat.get('utyp_id'), int) and self._utyp_id != dat['utyp_id']:
                self._utyp_id = dat['utyp_id']
                self._changed = True
            if self._dir_out is True and dat.get('val'):
                if len(self._val) == 0:
                    self._val.append(dat['val'])
                    self._changed = True
                else:
                    if self._val[0] != dat['val']:
                        self._val[0] = dat['val']
                        self._changed = True
