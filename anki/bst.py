""" Questions about binary search trees.
"""

class BinaryTreeNode:
    """ Standard binary search tree node.
    """
    __slots__ = "_element", "_left", "_right"

    def __init__(self, element, left=None, right=None):
        self._element = element
        self._left = left
        self._right = right

    def element(self):
        return self._element

    def left(self):
        return self._left

    def right(self):
        return self._right


def find_node_iterative(root: BinaryTreeNode, target) -> BinaryTreeNode:
    """ Using an iterative approach, write a function find_node(root, target) that returns the node with the given target value in a BST.

    :param root: root of the binary search tree.
    :param target:
    :return: node with the given target value
    """
    temp = root
    while temp is not None:
        if temp.element() == target:
            return temp
        elif target < temp.element():
            temp = temp.left()
        else:
            temp = temp.right()

    if temp is None:
        raise ValueError("Target not found")
    pass

