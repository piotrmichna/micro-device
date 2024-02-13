
from params import Param


class Module:
    def __init__(self, data: dict = {}):
        self._mid = 0
        self._chip_id = ''
        self._typ = ''
        self._typ_id = 0
        self._changed = False
        self._new = False
        self._sync_s = 0
        self._ticks_ms = 0
        self._params = []
        self._buss = None
        if data and isinstance(data, dict):
            self.m_dict = data

    @property
    def mid(self):
        return self._mid

    @property
    def chip_id(self):
        return self._chip_id

    @property
    def typ_id(self):
        return self._typ_id

    @property
    def is_changed(self):
        return self._changed

    @property
    def is_new(self):
        if len(self._params):
            for p in self._params:
                if p.is_new:
                    return True
        return False

    @property
    def typ(self):
        return self._typ

    @property
    def m_dict(self):
        self._changed = False
        params = []
        if len(self._params):
            for p in self._params:
                params.append(p.p_dict)
        return {'mid': self._mid, 'chip_id': self._chip_id,
                'typ': self._typ, 'typ_id': self._typ_id, 'params': params}

    @m_dict.setter
    def m_dict(self, dat):
        if isinstance(dat, dict):
            max_s = 0
            if isinstance(dat.get('mid'), int) and self._mid != dat['mid']:
                self._mid = dat['mid']
                self._changed = True
            if isinstance(dat.get('chip_id'), str) and self._chip_id != dat['chip_id']:
                self._chip_id = dat['chip_id']
                self._changed = True
            if isinstance(dat.get('typ'), str) and self._typ != dat['typ']:
                self._typ = dat['typ']
                self._changed = True
            if isinstance(dat.get('typ_id'), int) and self._typ_id != dat['typ_id']:
                self._typ_id = dat['typ_id']
                self._changed = True
            if isinstance(dat.get('sync_s'), int) and self._sync_s != dat['sync_s']:
                self._sync_s = dat['sync_s']
                max_s = self._sync_s
                self._changed = True
            if isinstance(dat.get('params'), list) and len(dat['params']):
                rv_ar = []
                for dp in dat['params']:
                    if isinstance(dp, dict):
                        pid = dp['pid'] if dp.get('pid') else None
                        nm = dp['name'] if dp.get('name') else None
                        app_flag = True
                        
                        for p in self._params:
                            if pid and isinstance(p, Param):       
                                # update param                         
                                if p.pid == pid:
                                    p.p_dict = dp
                                    if self._changed is False:
                                        self._changed = p.is_changed
                                    if p._sync_s > max_s:
                                        max_s = p._sync_s
                                    app_flag = False
                                    break
                            # remove param
                            elif isinstance(p, Param) and (p.pid>0) and (nm == p.name): 
                                rv_ar.append(p.pid)
                                app_flag = False
                                break
                        # add param
                        if app_flag is True:
                            self._params.append(Param(data=dp))
                            self._changed = True
                pk = 0
                if len(rv_ar):
                    for p in self._params:
                        if isinstance(p, Param) and (p.pid in rv_ar):
                            del self._params[pk]
                        pk += 1

                if max_s > self._sync_s:
                    self._sync_s = max_s
