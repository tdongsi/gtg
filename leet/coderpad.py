"""
Code snippets to write unit tests in coderpad.io
"""

import unittest

class MyTest(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(1, 1)

suite = unittest.defaultTestLoader.loadTestsFromTestCase(MyTest)
unittest.TextTestRunner().run(suite)
