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