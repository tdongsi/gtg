from unittest import TestCase

from anki.linkedlist import *


class TestListExercises(TestCase):

    def get_test_list(self):
        """ Returns a linked list: 2->1->3->4->5"""
        self._five = Node(5)
        self._four = Node(4, self._five)
        self._three = Node(3, self._four)
        self._one = Node(1, self._three)
        self._two = Node(2, self._one)
        return self._two

    def test_iterate_list(self):
        head = self.get_test_list()
        self.assertEqual(list(iterate_list(head)), [2,1,3,4,5])

    def test_reverse_list(self):
        head = self.get_test_list()
        expected = [2,1,3,4,5]
        expected.reverse()
        new_list = reverse_list(head)
        self.assertEqual(list(iterate_list(new_list)), expected)

    def test_find_list(self):
        head = self.get_test_list()
        self.assertEqual(find_item(head, 2), head)
        self.assertEqual(find_item(head, 5), self._five)
        self.assertEqual(find_item(head, 0), None)
        self.assertEqual(find_item(None, 0), None)

    def test_appendleft(self):
        head = self.get_test_list()
        new_list = appendleft(head, 7)
        self.assertEqual(list(iterate_list(new_list)), [7, 2, 1, 3, 4, 5])

        new_list = appendleft(None, 8)
        self.assertEqual(list(iterate_list(new_list)), [8])

        new_list = appendleft(self._five, 9)
        self.assertEqual(list(iterate_list(new_list)), [9, 5])