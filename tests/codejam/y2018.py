
import unittest
import codejam.y2018 as cj

class SaveTheUniverse(unittest.TestCase):

    def test_compute_damage(self):
        solver = cj.SaveTheUniverse('random.txt')
        self.assertEqual(solver._compute_damage('SCCSSC'), 9)
        self.assertEqual(solver._compute_damage('SCSCSC'), 7)
        self.assertEqual(solver._compute_damage('SCSSCC'), 5)

    def test_compute(self):
        solver = cj.SaveTheUniverse('random.txt')
        self.assertEqual(solver._compute(1, 'CS'), 1)
        self.assertEqual(solver._compute(2, 'CS'), 0)
        self.assertEqual(solver._compute(6, 'SCCSSC'), 2)
        self.assertEqual(solver._compute(3, 'CSCSS'), 5)