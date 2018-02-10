# From project root run:
# python -m unittest tests/file_scan_test.py

import unittest

from iterators.file_scan import FileScan

class TestFileScan(unittest.TestCase):

    def test_scan(self):
        fs = FileScan('movie_test_data.csv')
        test_result = []
        row1 = ['1', 'Toy Story (1995)', 'Adventure|Animation|Children|Comedy|Fantasy']
        row2 = ['2', 'Jumanji (1995)', 'Adventure|Children|Fantasy']
        row3 = ['3', 'Grumpier Old Men (1995)', 'Comedy|Romance']
        expected = [row1, row2, row3]

        for row in fs:
            test_result.append(row)

        fs.close_file()

        assert(test_result) == expected
