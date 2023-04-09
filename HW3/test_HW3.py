import unittest

from HW3 import delete_space

delete_space (" fgfd")


class Testmult(unittest.TestCase):
    def test_delete_space(self):
        self.assertEqual(delete_space(" HELLO "), "HELLO")
