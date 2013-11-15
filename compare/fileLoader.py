#coding: utf-8


from data import data


class wrapper(object):
    def __init__(self, data):
        self.vals = data


class fileLoader(object):
    def __init__(self, fileName, sep='\t', key=0):
        self._lns = dict()
        self._file_name = fileName
        self._key_pos = key
        self._sep = sep

    def load(self):
        fp = open(self._file_name, 'r')

        def get_file(fp):
            for line in fp.readlines():
                yield line

        for line in get_file(fp):
            entry = data(line, self._sep, self._key_pos)
            self._lns[entry.key()] = entry

        fp.close()

    def __getitem__(self, index):
        return wrapper(self._lns.get(index))
