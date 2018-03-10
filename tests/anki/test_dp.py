
import unittest

import anki.dp as dp

class TestDpExcercises(unittest.TestCase):

    def test_subset_sum(self):

        self.assertEqual(True, dp.subset_sum([2, 3, 7, 8], 11))
        self.assertEqual(True, dp.subset_sum([3, 34, 4, 12, 5, 2], 9))

    def test_longest_common_subsequence_length(self):

        self.assertEqual(3, dp.longest_common_subsequence_length("ABCDGH", "AEDFHR"))
        self.assertEqual(4, dp.longest_common_subsequence_length("AGGTAB", "GXTXAYB"))

    def test_longest_common_subsequence(self):
        self.assertEqual("ADH", dp.longest_common_subsequence("ABCDGH", "AEDFHR"))
        self.assertEqual("GTAB", dp.longest_common_subsequence("AGGTAB", "GXTXAYB"))