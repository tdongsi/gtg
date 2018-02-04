
import random
import unittest

from anki.sort import heap_sort as do_sort
import anki.sort


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
        self.assertEqual(anki.sort.binary_search(None, 1), -1)
        self.assertEqual(anki.sort.binary_search([], 1), -1)
        self.assertEqual(anki.sort.binary_search([1,2,3,4,5], 3), 2)
        self.assertEqual(anki.sort.binary_search([1,2,3,4,5], 6), -1)

    def test_search_iterative(self):
        self.assertEqual(anki.sort.binary_search_iterative(None, 1), -1)
        self.assertEqual(anki.sort.binary_search_iterative([], 1), -1)
        self.assertEqual(anki.sort.binary_search_iterative([1,2,3,4,5], 3), 2)
        self.assertEqual(anki.sort.binary_search_iterative([1,2,3,4,5], 6), -1)

    def test_search_repeated(self):
        self.assertTrue(anki.sort.binary_search_iterative([1, 2, 2, 3, 4, 5, 6, 7], 2) in [1, 2])
        self.assertTrue(anki.sort.binary_search_iterative([1, 1, 2, 2, 2, 3, 3, 4], 2) in [2, 3, 4])
        self.assertTrue(anki.sort.search_start([2, 2], 2) in [0, 1])

    def test_search_start(self):
        self.assertEqual(anki.sort.search_start(None, 1), -1)
        self.assertEqual(anki.sort.search_start([], 1), -1)
        self.assertEqual(anki.sort.search_start([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(anki.sort.search_start([1, 2, 3, 4, 5], 6), -1)

        self.assertEqual(anki.sort.search_start([1, 2, 2, 3, 4, 5, 6, 7], 2), 1)
        self.assertEqual(anki.sort.search_start([1, 1, 2, 2, 2, 3, 3, 4], 2), 2)
        self.assertEqual(anki.sort.search_start([2, 2], 2), 0)

    def test_search_end(self):
        self.assertEqual(anki.sort.search_end(None, 1), -1)
        self.assertEqual(anki.sort.search_end([], 1), -1)
        self.assertEqual(anki.sort.search_end([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(anki.sort.search_end([1, 2, 3, 4, 5], 6), -1)

        self.assertEqual(anki.sort.search_end([1, 2, 2, 3, 4, 5, 6, 7], 2), 2)
        self.assertEqual(anki.sort.search_end([1, 1, 2, 2, 2, 3, 3, 4], 2), 4)
        self.assertEqual(anki.sort.search_end([2, 2], 2), 1)