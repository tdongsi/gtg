""" Questions about binary search trees.
"""

# Just for testing
INTEGER_MIN = -2**32
INTEGER_MAX = 2*32

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


def is_bst(root:BinaryTreeNode, min=INTEGER_MIN, max=INTEGER_MAX) -> bool:
    """ Check if a given tree is a Binary Search Tree.
    """
    if (root.element() >= max or root.element() <= min):
        return False
    else:
        check = True
        if root.left():
            check &= is_bst(root.left(), min, root.element())
        if root.right():
            check &= is_bst(root.right(), root.element(), max)
        return check


def get_height(node:BinaryTreeNode) -> int:
    """ Get the height in nodes of a BST
    """
    if node is None:
        return 0
    else:
        return 1 + max(get_height(node.left()), get_height(node.right()))