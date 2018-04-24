from unittest import TestCase
import os

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
        self.assertEqual(Box.complex_string("22+(2-4)"), 20)
        self.assertEqual(Box.complex_string("(2-4)"), -2)
        self.assertEqual(Box.complex_string("(4)"), 4)


class TestGoogle(TestCase):

    def test_word_puzzle(self):
        GoogleWordPuzzle.RESOURCE_FOLDER = os.getcwd() + "/resources"
        # self.assertEqual(['mold', 'mole', 'male', 'mace', 'mach', 'each', 'etch'], Google.word_puzzle("mold", "etch"))
        # print(Google.word_puzzle("accent", "sprint"))
        # print(Google.word_puzzle("hello", "class"))
        print(GoogleWordPuzzle.word_puzzle("damp", "like"))


class TestFacebook(TestCase):

    def test_permutations(self):

        import itertools
        perms = itertools.permutations([1, 2, 3, 4])
        for perm in perms:
            # print(perm)
            pass

        perms = FacebookPerms.generate_perms([1, 2, 3, 4])
        for perm in perms:
            print(perm)


class TestLinkedIn(TestCase):

    def test_min_word_dist(self):
        words = "the quick brown fox quick jumps".split()
        self.assertEqual(LinkedIn.min_word_dist(words, "fox", "quick"), 1)
