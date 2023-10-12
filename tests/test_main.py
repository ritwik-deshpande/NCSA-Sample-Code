import unittest
from main import check_vowels, transform

class TestMain(unittest.TestCase):

    def test_check_vowel_true(self):
        self.assertEqual(True, check_vowels('a'))

    def test_check_vowel_false(self):
        self.assertEqual(False, check_vowels('z'))

    def test_transform(self):
        self.assertEqual("1", transform('a'))
        self.assertEqual("5", transform('e'))

    def test_transform_failure(self):
        with self.assertRaises(Exception):
            transform('4')

        with self.assertRaises(Exceptionig):
            transform('t')
