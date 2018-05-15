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

    def test_union(self):
        self.assertEqual(LinkedIn.union(None, None), None)
        self.assertEqual(LinkedIn.union(None, [1]), set([1]))
        self.assertEqual(LinkedIn.union([1], None), set([1]))

        self.assertEqual(LinkedIn.union([], []), set())
        self.assertEqual(LinkedIn.union([], [1]), set([1]))
        self.assertEqual(LinkedIn.union([1], []), set([1]))

        self.assertEqual(LinkedIn.union([1, 2], [3, 4]), set([1, 2, 3, 4]))

        self.assertEqual(LinkedIn.union([1, 2], [1, 2]), set([1, 2]))
        self.assertEqual(LinkedIn.union([1, 1, 2], [2, 2, 3]), set([1, 2, 3]))

        a = [int(e) for e in "1 3 3 4 5 5 8".split()]
        b = [int(e) for e in "3 4 7 7 8".split()]
        self.assertEqual(LinkedIn.intersect(a, b), [3, 4, 8])


class TestAirbnb(TestCase):

    def test_triangle(self):
        a = [7, 10, 7]
        b = [2, 3, 4]
        c = [2, 7, 4]

        res = triangleOrNot(a, b, c)
        print(res)

    def test_consecutive(self):
        self.assertEqual(consecutive(15), 3)
        self.assertEqual(consecutive(10), 1)
        self.assertEqual(consecutive(250), 3)

    def test_create_text(self):
        self.assertFalse(create_text_from_magazine("Hello World", "The quick brown fox jumps over the lazy dog"))
        self.assertTrue(create_text_from_magazine("Hell", "Hello"))

