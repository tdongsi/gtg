from unittest import TestCase

from leet.string import *


class TestBox(TestCase):

    def test_simple_string(self):

        self.assertEqual(Box.simple_string("5+6-12"), -1)
        self.assertEqual(Box.simple_string(""), 0)
        self.assertEqual(Box.simple_string("5"), 5)
        self.assertEqual(Box.simple_string("-5+6"), 1)