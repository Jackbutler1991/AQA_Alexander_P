import unittest

from .while_loops import *


class Testmult(unittest.TestCase):
    def test_mult(self):
        self.assertEqual(mult(5), 120)
        self.assertEqual(mult(1), 1)

    def test_mult1(self):
        self.assertRaises(ValueError, mult, "a")
        self.assertRaises(ValueError, mult, (1, 2))
        self.assertRaises(ValueError, mult, -1)
        self.assertRaises(ValueError, mult, 12.3)

    def test_sq_flow(self):
        self.assertEqual(sq_flow(1, 1), 7)
        self.assertEqual(sq_flow(1, 512), 1)
        self.assertEqual(sq_flow(512, 1), 23)
        self.assertEqual(sq_flow(512, 1024), 5)
        self.assertEqual(sq_flow(1024, 512), 9)
        self.assertEqual(sq_flow(0, 1), 1)

    def test_sq_flow_Errors(self):
        self.assertRaises(ValueError, sq_flow, "a", 0)
        self.assertRaises(ValueError, sq_flow, 0, 0)
        self.assertRaises(ValueError, sq_flow, (1, 2, "№"), 0)
