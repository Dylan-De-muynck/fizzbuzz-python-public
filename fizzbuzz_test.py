import unittest
from fizzbuzz import *
class FizzBuzzTest(unittest.TestCase):

    def test_nombre_est_zero(self):
        with self.assertRaises(ArgurmentError):
            FizzBuzz.isFizzOrBuzz(0)
    
    def test_nombre_est_negatif(self):
        with self.assertRaises(ArgurmentError):
            FizzBuzz.isFizzOrBuzz(-1)

    def test_nombre_est_multiple_de_3_donne_fizz(self):
        nb = 6
        self.assertEqual(FizzBuzz.isFizzOrBuzz(nb), "Fizz")

