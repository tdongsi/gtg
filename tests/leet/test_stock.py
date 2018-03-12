
import unittest
import leet.stock as ls

class TestStock(unittest.TestCase):

    def test_maximal_subarray(self):
        self.assertEqual([4, -1, -2, 1, 5], ls.maximum_subarray([-2, -3, 4, -1, -2, 1, 5, -3]))
        self.assertEqual([4, -1, 2, 1], ls.maximum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
        self.assertEqual([5, -2, 9], ls.maximum_subarray([1, -3, 5, -2, 9, -8, -6, 4]))
        pass

    