
import random
import unittest

from anki.sort import heap_sort as do_sort
from anki.sort import binary_search


class TestSorting(unittest.TestCase):

    def test_sort(self):
        # import sorting function as do_sort
        for i in range(1, 20):
            # Do it 5 times
            expected = list(range(i))
            for i in range(5):
                mlist = expected[:]
                random.shuffle(mlist)
                # print mlist
                self.assertEqual(do_sort(mlist), expected)

        pass

    def test_same_element(self):

        self.assertEqual(do_sort([2, 3, 5, 7, 4, 2, 6, 1]), [1, 2, 2, 3, 4, 5, 6, 7])
        self.assertEqual(do_sort([2, 2]), [2, 2])
        self.assertEqual(do_sort([1, 2, 1]), [1, 1, 2])
        self.assertEqual(do_sort([2, 3, 1, 2, 2, 4, 3, 1]), [1, 1, 2, 2, 2, 3, 3, 4])
        self.assertEqual(do_sort([2, 1]), [1, 2])
        pass


class TestBinarySearch(unittest.TestCase):

    def test_search(self):
        self.assertEqual(binary_search(None, 1), -1)
        self.assertEqual(binary_search([], 1), -1)
        self.assertEqual(binary_search([1,2,3,4,5], 3), 2)
        self.assertEqual(binary_search([1,2,3,4,5], 6), -1)