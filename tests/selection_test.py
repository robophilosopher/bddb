import unittest

from iterators.selection import Selection
from iterators.file_scan import FileScan

class TestSelection(unittest.TestCase):
    def test_selection(self):
        predicate = lambda r: 'Toy Story (1995)' in r
        expected = [['1', 'Toy Story (1995)', 'Adventure|Animation|Children|Comedy|Fantasy']]
        results = []
        fs = FileScan("movie_test_data.csv")
        s = Selection(fs, predicate)

        for row in s:
            results.append(row)

        s.close_file()

        assert(results) == expected

