from abc import ABCMeta, abstractmethod

class SequenceIterator:
    """An iterator for Python sequence type"""

    def __init__(self, sequence):
        self._seq = sequence
        self._k = -1

    def __next__(self):
        self._k += 1

        if self._k < len(self._seq):
            return self._seq[self._k]
        else:
            raise StopIteration()

    def __iter__(self):
        """By convention, iterator must return itself as an iterator"""
        return self


class Sequence(metaclass=ABCMeta):
    """Simulate collections.Sequence"""

    @abstractmethod
    def __len__(self):
        """Return the length of the sequence"""

    @abstractmethod
    def __getitem__(self, j):
        """Return the element at index j"""

    def __contains__(self, item):
        """Concrete behavior based on abstract methods"""
        for j in range(len(self)):
            if self[j] == item:
                return True

        return False
