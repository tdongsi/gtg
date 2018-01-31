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

    def test_find_node_recursive(self):
        self.assertEqual(self._A, find_node_recursive(self._root, 2))
        self.assertEqual(self._E, find_node_recursive(self._root, 15))
        self.assertEqual(None, find_node_recursive(self._root, 17))

    def test_is_bst(self):
        self.assertTrue(is_bst(self._root))

        # Create a negative case of BST
        self._A = BinaryTreeNode(2)
        self._B = BinaryTreeNode(11)
        self._C = BinaryTreeNode(12)

        self._D = BinaryTreeNode(5, self._A, self._B)
        self._E = BinaryTreeNode(15, self._C)

        self._root = BinaryTreeNode(10, self._D, self._E)
        self.assertFalse(is_bst(self._root))

    def test_get_height(self):
        self.assertEqual(3, get_height(self._root))

        # add more node into the tree
        Cp = BinaryTreeNode(11)
        self._C._left = Cp  # dirty quick way
        self.assertTrue(is_bst(self._root))
        self.assertEqual(4, get_height(self._root))

    def test_insert_node_iterative(self):
        root = None
        new_root = insert_node_iterative(root, 10)
        self.assertEqual(new_root, BinaryTreeNode(10))

        new_root = insert_node_iterative(self._root, 17)
        # TODO: print out

    pass
