from iterators.iterator import Iterator

class Projection(Iterator):
    def __init__(self, node, projectingf):
        self._inputs = node
        self.projectingf = projectingf

    def __next__(self):
        record = next(self._inputs)
        print(record)
        return self.projectingf(record)
