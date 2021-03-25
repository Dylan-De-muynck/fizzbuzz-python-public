import unittest
from fizzbuzz import *
class FizzBuzzTest(unittest.TestCase):

    def test_nombre_est_zero(self):
        with self.assertRaises(ArgurmentError):
            FizzBuzz.isFizzOrBuzz(0)
