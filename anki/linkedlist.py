
class Node:
    __slots__ = "_element", "_next"

    def __init__(self, val, next_node=None):
        self._element = val
        self._next = next_node

    def element(self):
        return self._element

    def get_next(self):
        return self._next

    def set_next(self, next_node):
        self._next = next_node


def reverse_list(head:Node) -> Node:
    """ Write a function that reverses a linked list

    :param head: The head of the linked list.
    :return: The new head of the reversed list.
    """
    prev = None
    cur = head

    while cur is not None:
        temp = cur
        cur = cur.get_next()
        temp.set_next(prev)
        prev = temp

    return prev


def iterate_list(head:Node):
    """ Iterate a linked list"""
    cur = head
    while cur is not None:
        yield cur.element()
        cur = cur.get_next()


def find_item(head:Node, target)->Node:
    """Find item in the given linked list"""
    cur = head
    while cur is not None:
        if cur.element() == target:
            return cur
        else:
            cur = cur.get_next()
    # Should be None here
    return cur


def appendleft(head:Node, item)->Node:
    """ Insert an item at the head of linked list.
    :return: The head of new list
    """
    nd = Node(item, head)
    return nd
