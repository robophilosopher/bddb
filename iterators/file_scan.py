import csv
from iterators.iterator import Iterator

class FileScan(Iterator):
    def __init__(self, db_file_name):
        self.f = open(db_file_name, 'r')
        self.reader = csv.reader(self.f)
        next(self.reader)

    def __next__(self):
        return next(self.reader)

    # Test helper method to make warning go away.
    # Might be otherwise useless.
    def close_file(self):
        self.f.close()


