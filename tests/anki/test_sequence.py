
import unittest

import anki.sequence as seq

class TestQueue(unittest.TestCase):

    def test_queue(self):

        queue = seq.Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        self.assertEqual(1, queue.dequeue())
        self.assertEqual(2, queue.dequeue())

        queue.enqueue(4)
        queue.enqueue(5)
        self.assertEqual(3, queue.dequeue())