"""
Array, Stack, Queue, Deque.
"""

class Queue():
    """Classic interview question: Queue using Stacks."""

    def __init__(self):
        self._incoming = []
        self._outgoing = []

    def enqueue(self, item):
        while self._outgoing:
            self._incoming.append(self._outgoing.pop())
        self._incoming.append(item)

    def dequeue(self):
        while self._incoming:
            self._outgoing.append(self._incoming.pop())

        return self._outgoing.pop()

    def __str__(self):
        while self._outgoing:
            self._incoming.append(self._outgoing.pop())

        return str(self._incoming)