from unittest import TestCase

from anki.bit import *


class TestBitExercises(TestCase):

    def test_hamming_distance(self):
        """ From https://en.wikipedia.org/wiki/Hamming_distance
        """
        self.assertEqual(3, hamming_distance("karolin", "kathrin"))
        self.assertEqual(3, hamming_distance("karolin", "kerstin"))
        self.assertEqual(3, hamming_distance("2173896", "2233796"))

    def test_hamming_distance_int(self):
        self.assertEqual(2, hamming_distance_int(0b1011101, 0b1001001))

    def test_add(self):
        self.assertEqual(5, add(5, 0))
        self.assertEqual(5, add(0, 5))
        self.assertEqual(0, add(0, 0))
        self.assertEqual(5, add(2, 3))
        self.assertEqual(6, add(3, 3))

    def test_subtract(self):
        self.assertEqual(5, subtract(5, 0))
        # self.assertEqual(-5, subtract(0, 5))
        self.assertEqual(0, subtract(0, 0))
        self.assertEqual(1, subtract(3, 2))
        self.assertEqual(0, subtract(3, 3))

    def test_others(self):
        # Turn off the 3rd bit from the end
        x = 0b1011101
        self.assertEqual(0b1011001, x & ~(1 << 2))