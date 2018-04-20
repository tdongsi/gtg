
import unittest

import chapter13.string as gtg


class TestString(unittest.TestCase):

    def test_pattern_matching(self):

        self.assertEqual(gtg.find_brute('ANPANMAN', 'PAN'), 2)
        self.assertEqual(gtg.find_brute('abacaabaccabacabaabb', 'abacab'), 10)