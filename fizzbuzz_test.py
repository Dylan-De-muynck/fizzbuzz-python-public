import unittest
from fizzbuzz import *
class FizzBuzzTest(unittest.TestCase):

    def test_nombre_est_zero_leve_erreur(self):
        with self.assertRaises(ArgurmentError):
            FizzBuzz.isFizzOrBuzz(0)
    
    def test_nombre_est_negatif_leve_erreur(self):
        with self.assertRaises(ArgurmentError):
            FizzBuzz.isFizzOrBuzz(-1)

    def test_nombre_est_multiple_de_3_donne_fizz(self):
        nb = 6
        actual = "Fizz"
        self.assertEqual(FizzBuzz.isFizzOrBuzz(nb), actual)

    def test_nombre_est_multiple_de_5_donne_buzz(self):
        nb = 20
        actual = "Buzz"
        self.assertEqual(FizzBuzz.isFizzOrBuzz(nb), actual)

    def test_nombre_est_multiple_de_3_et_de_5_donne_fizzbuzz(self):
        nb = 15
        actual = "FizzBuzz"
        self.assertEqual(FizzBuzz.isFizzOrBuzz(nb), actual)

    def test_aucun_des_autres_cas_precedent_donne_le_nombre_lui_meme(self):
        nb = 23
        self.assertEqual(FizzBuzz.isFizzOrBuzz(nb), nb)

if __name__ == '__main__':
    unittest.main()
