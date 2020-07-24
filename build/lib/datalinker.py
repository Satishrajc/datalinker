#!/usr/bin/python
"""
Description: Data sharing mechanism between the python files across the process
"""

class global_buffer(dict):
    """
    This will create the global space to save the data which can be accessed across the python script
    """
    def __init__(self, *args, **kwargs):
        dict.__init__(self)
        self.update_dict(*args, **kwargs)
        self._data = 'global'

    def update_dict(self, *args, **kwargs):
        for k, v in dict(*args, **kwargs).items():
            self[k] = v

class DataLinkerMain(global_buffer):
    """TBD"""
    def __init__(self):
        global_buffer.__init__(self)

    def set(self, buffer, value):
        if self._data in self:
            self[self._data][buffer] = value
        else:
            self[self._data] = global_buffer({buffer: value})

    def get(self, buffer):
        existing_data_names = self._data in self and buffer in self[self._data]
        if existing_data_names:
            return self[self._data][buffer]
        return None

class DataLinker(object):
    DataSharing_object = DataLinkerMain()
    def run(self): return self.DataSharing_object
