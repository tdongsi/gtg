
import unittest
import hackerrank.Encircular


class MyTest(unittest.TestCase):

    def test_cases(self):
        _input = ["GRGL", "G", "L"]

        hackerrank.Encircular.doesCircleExist(_input)
