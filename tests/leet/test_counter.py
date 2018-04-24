
import unittest
from leet.counter import *


class TestCounter(unittest.TestCase):

    def test_find_uniques(self):
        self.assertEqual(find_uniques([1,1,2,3,4,4]), [2,3])
        pass

    def test_permutations(self):
        for perm in permutations([1,2,3,4]):
            print(perm)

        all_perms = list(permutations([1,2,3]))
        print(all_perms)