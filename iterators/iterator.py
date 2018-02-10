class Iterator(object):
    def __init__(self):
        self._inputs = []

    def __iter__(self):
        return self

    def __next__(self):
        raise Exception('Implement __next___')

