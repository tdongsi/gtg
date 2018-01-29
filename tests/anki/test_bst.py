from unittest import TestCase

from anki.bst import *


class TestBstExercises(TestCase):

    def setUp(self):
        """ Create a test BST.
        """
        self._A = BinaryTreeNode(2)
        self._B = BinaryTreeNode(7)
        self._C = BinaryTreeNode(12)

        self._D = BinaryTreeNode(5, self._A, self._B)
        self._E = BinaryTreeNode(15, self._C)

        self._root = BinaryTreeNode(10, self._D, self._E)

        pass

    def test_find_node_iterative(self):
        self.assertEqual(self._A, find_node_iterative(self._root, 2))
        self.assertEqual(self._E, find_node_iterative(self._root, 15))

    def test_find_node_iterative_none(self):
        with self.assertRaises(ValueError, msg="Target not found") as context:
            find_node_iterative(self._root, 17)

    pass
