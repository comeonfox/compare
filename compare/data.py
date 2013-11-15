#coding: utf-8


class data(object):
    '''
    A data class, to describe the data to be compared.
    '''
    def __init__(self, line, sep='\t', key=0):
        '''
        line: a line in a ascii text file, usually are `sep` seperated values.
        sep: seperator to split line.
        key: index of the field of the key in line.
        '''
        _tmp_data = line.strip().split(sep)
        self._key = _tmp_data.pop(int(key))
        self._vals = _tmp_data

    def __get__(self, instance, owner):
        return self._vals

    def __set__(self, instance, value):
        '''
        the __set__ method is banned.
        '''
        raise AttributeError

    def key(self):
        return self._key
