#!/usr/bin/python
import deprecation

"""
Description: 
Data sharing mechanism between the python files across the process
"""
__version__ = '2.1.1'


class GlobalBuffer(dict):
    """
    This will create the global space to save the data which can be accessed across the python script
    """
    def __init__(self, *args, **kwargs):
        dict.__init__(self)
        self.update_inbuilt_dict(*args, **kwargs)
        self._data = 'global'

    def update_inbuilt_dict(self, *args, **kwargs):
        for key, value in dict(*args, **kwargs).items():
            self[key] = value


class Main(GlobalBuffer):
    """This is the mail class which updates/fetches data from/to global dict"""
    def __init__(self):
        super().__init__()

    # Pushing data to global dictionary
    def push(self, buffer, value):
        if self._data in self:
            self[self._data][buffer] = value
        else:
            self[self._data] = GlobalBuffer({buffer: value})

    # Retrieving data back from global dictionary
    def pop(self, buffer):
        existing_data_names = self._data in self and buffer in self[self._data]
        if existing_data_names:
            return self[self._data][buffer]
        return None

    @deprecation.deprecated(deprecated_in="0.0.2", removed_in="0.0.2",
                            current_version=__version__,
                            details="Use the push() instead of set() instead")
    def set(self, buffer, value):
        return self.push(buffer, value)

    @deprecation.deprecated(deprecated_in="0.0.2", removed_in="0.0.2",
                            current_version=__version__,
                            details="Use the pop() instead of get() instead")
    def get(self, buffer):
        return self.pop(buffer)


class DataLinker(Main):
    DataSharing_object = Main()

    def run(self):
        return self.DataSharing_object
