import unittest

from iterators.selection import Selection
from iterators.file_scan import FileScan
from iterators.projection import Projection

class TestSelection(unittest.TestCase):
    def test_selection(self):
        # current csv schema is 0:movieId, 1:title, 2:genres
        pf = lambda r: r[1] # gimme the movie titles
        fs = FileScan('movie_test_data.csv')
        p = Projection(fs, pf)
        
        expected = ['Toy Story (1995)', 'Jumanji (1995)', 'Grumpier Old Men (1995)']
        result = []

        for record in p:
            result.append(record)

        fs.close_file()

        assert(result) == expected
