
from unittest import TestCase

from leet.medium import *


class MedianSortedArraysTest(TestCase):

    def test_cases(self):
        sol = MedianSortedArrays()
        self.assertEqual(sol.findMedianSortedArrays([1, 3], [2]), 2.0)
        self.assertEqual(sol.findMedianSortedArrays([1, 2], [3, 4]), 2.5)
        self.assertEqual(sol.findMedianSortedArrays([1, 2], [1, 2]), 1.5)
        self.assertEqual(sol.findMedianSortedArrays([1], [1]), 1.0)
        # self.assertEqual(sol.findMedianSortedArrays([1, 3], [2, 4]), 2.5)

        self.assertEqual(sol._find_k([1, 2], [1, 2], 2), 2)
        self.assertEqual(sol._find_k([1], [1], 0), 1)
        self.assertEqual(sol._find_k([1, 3], [2, 4], 2), 3)
        pass


class MyTest(TestCase):

    def test_longest_consecutive(self):
        sol = LongestConsecutive()
        self.assertEqual(sol.longest_consecutive([100, 4, 200, 1, 3, 2]), 4)
        pass

    def test_longest_substring(self):
        sol = LongestSubstringDistinctChars()
        self.assertEqual(sol.longest_substring("abcbbbbcccbdddadacb", 2), "bcbbbbcccb")
        self.assertEqual(sol.longest_substring("abcadcacacaca", 3), "cadcacacaca")

        self.assertEqual(sol.longest_substring("aabbcc", 1), "aa")
        self.assertEqual(sol.longest_substring("aabbcc", 2), "aabb")
        self.assertEqual(sol.longest_substring("aabbcc", 3), "aabbcc")
        pass
