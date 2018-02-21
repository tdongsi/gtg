from unittest import TestCase

from leet.string import *


class TestBox(TestCase):

    def test_simple_string(self):

        self.assertEqual(Box.simple_string("5+6-12"), -1)
        self.assertEqual(Box.simple_string(""), 0)
        self.assertEqual(Box.simple_string("5"), 5)
        self.assertEqual(Box.simple_string("-5"), -5)
        self.assertEqual(Box.simple_string("-5+6"), 1)

    def test_simple_string_serious(self):

        self.assertEqual(Box.simple_string_serious("5+6-12"), -1)
        self.assertEqual(Box.simple_string_serious(""), 0)
        self.assertEqual(Box.simple_string_serious("5"), 5)
        self.assertEqual(Box.simple_string_serious("-5"), -5)
        self.assertEqual(Box.simple_string_serious("-5+6"), 1)

    def test_complex_string(self):

        self.assertEqual(Box.complex_string("5+6-12"), -1)
        self.assertEqual(Box.complex_string(""), 0)
        self.assertEqual(Box.complex_string("5"), 5)
        self.assertEqual(Box.complex_string("-5"), -5)
        self.assertEqual(Box.complex_string("-5+6"), 1)

        self.assertEqual(Box.complex_string("5+16-((9-6)-(4-2))"), 20)
        self.assertEqual(Box.complex_string("22+(2-4)"))