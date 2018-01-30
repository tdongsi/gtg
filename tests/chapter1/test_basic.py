from unittest import TestCase

import chapter1.basic


class TestExercises(TestCase):

    def test_factors(self):
        self.assertEqual([1,100,2,50,4,25,5,20,10], list(chapter1.basic.factors(100)))