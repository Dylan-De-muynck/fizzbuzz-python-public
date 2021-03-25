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

    def test_nombre_est_multiple_de_5_donne_buzz(self):
        nb = 20
        self.assertEqual(FizzBuzz.isFizzOrBuzz(nb), "Buzz")

    def test_nombre_est_multiple_de_3_et_de_5_donne_fizzbuzz(self):
        nb = 15
        self.assertEqual(FizzBuzz.isFizzOrBuzz(nb), "FizzBuzz")

    def test_aucun_des_autres_cas_precedent_donne_le_nombre_lui_meme(self):
        nb = 23
        self.assertEqual(FizzBuzz.isFizzOrBuzz(nb), nb)

