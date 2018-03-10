
import unittest

import anki.dp as dp

class TestDpExcercises(unittest.TestCase):

    def test_subset_sum(self):

        self.assertEqual(True, dp.subset_sum({2, 3, 7, 8}, 11))
        self.assertEqual(True, dp.subset_sum({3, 34, 4, 12, 5, 2}, 9))