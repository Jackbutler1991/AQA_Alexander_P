import unittest
from while_loops import mult


#mult(9)
class Testmult(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(mult(5), 120)

    def test_sum1(self):
        self.assertRaises(ValueError, mult, "a")

    def test_sum2(self):
        self.assertRaises(ValueError, mult, -1)

