
import unittest

import leet.histogram as hg

class TestHistogram(unittest.TestCase):

    def test_largest_rect_histogram(self):
        self.assertEqual(hg.largest_rect_histogram_DnC([6, 2, 5, 4, 5, 1, 6]), 12)
        self.assertEqual(hg.largest_rect_histogram_DnC([4,6,5,1,3,2]), 12)
        pass
