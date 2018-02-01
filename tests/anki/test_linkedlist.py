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

    