
import unittest
import codejam.y2018 as cj

class SaveTheUniverse(unittest.TestCase):

    def test_compute_damage(self):
        solver = cj.SaveTheUniverse('random.txt')
        self.assertEqual(solver._compute_damage('SCCSSC'), 9)
        self.assertEqual(solver._compute_damage('SCSCSC'), 7)
        self.assertEqual(solver._compute_damage('SCSSCC'), 5)