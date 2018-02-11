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

    def set_left(self, left):
        self._left = left

    def set_right(self, right):
        self._right = right

    def __eq__(self, other):
        return self._element == other._element and self._left == other._left and self._right == other._right


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


def find_min(root:BinaryTreeNode) -> int:
    """Find minimum value in a BST"""
    if root is None:
        return None

    curr = root
    while curr is not None:
        if curr.left() is not None:
            curr = curr.left()
        else:
            return curr.element()


def find_successor(root: BinaryTreeNode, target) -> int:
    """Get the successor of a value in a BST rooted by given node. Returns int."""
    if root is None:
        return None

    prev = None
    curr = root

    while curr is not None:
        if curr.element() == target:
            if curr.right() is not None:
                return find_min(curr.right())
            else:
                if prev is not None and prev.element() > target:
                    return prev.element()
                else:
                    return None
        elif curr.element() < target:
            # prev = curr  # TRICKY: enabling this is a bug
            curr = curr.right()
        else:
            prev = curr
            curr = curr.left()

    return None


def find_node_recursive(root:BinaryTreeNode, target) -> BinaryTreeNode:
    """ Using a recursive approach, write a function find_node(root, target) that returns the node with the given target value in a BST.
    """
    if root is None:
        return None
    elif root.element() == target:
        return root
    elif root.element() < target:
        return find_node_recursive(root.right(), target)
    else:
        return find_node_recursive(root.left(), target)


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


def insert_node_iterative(root:BinaryTreeNode, target) -> BinaryTreeNode:
    """Using an iterative approach, insert a value into a BST: insert(node, int)"""
    temp = root
    while temp is not None:
        if temp.element() == target:
            raise ValueError
        elif temp.element() < target:
            if temp.right() is None:
                temp.set_right(BinaryTreeNode(target))
                return root
            else:
                temp = temp.right()
        else:
            if temp.left() is None:
                temp.set_left(BinaryTreeNode(target))
                return root
            else:
                temp = temp.left()

    # root is None: empty tree
    if root is None:
        return BinaryTreeNode(target)


def insert_node_recursive(root:BinaryTreeNode, target) -> BinaryTreeNode:
    """Using a recursive approach, insert a value into a BST: insert(node, int).
    Return None if no new tree is created.
    """
    # TODO: better way?
    if root is None:
        return BinaryTreeNode(target)
    else:
        if root.element() == target:
            raise ValueError("Value already exists")
        elif root.element() < target:
            if root.right() is None:
                root.set_right(BinaryTreeNode(target))
                return None
            else:
                insert_node_recursive(root.right(), target)
        else:
            if root.left() is None:
                root.set_left(BinaryTreeNode(target))
                return None
            else:
                insert_node_recursive(root.left(), target)
    pass
