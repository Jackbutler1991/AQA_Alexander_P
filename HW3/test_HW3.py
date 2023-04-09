import unittest

from HW3 import delete_space


class Testmult(unittest.TestCase):
    def test_delete_space(self):
        self.assertEqual(delete_space(" HELLO "), "HELLO")
        self.assertEqual(delete_space("HELLO"), "HELLO")
        self.assertEqual(delete_space(" 123 "), "123")
        self.assertEqual(delete_space(" H "), "H")
        self.assertEqual(delete_space(" HyYy123@ "), "HyYy123@")
        self.assertEqual(delete_space(" Привет "), "Привет")
        self.assertEqual(delete_space(" Hello World  "), "Hello World")

    def test_delete_space_Errors(self):
        self.assertRaises(ValueError, delete_space, 12.3)
        self.assertRaises(ValueError, delete_space, 2)
        self.assertRaises(ValueError, delete_space, (1, 12, "str"))
        self.assertRaises(ValueError, delete_space, "")
