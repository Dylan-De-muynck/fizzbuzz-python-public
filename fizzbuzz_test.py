import unittest
class FizzBuzzTest(unittest.TestCase):

    def test_nombre_est_zero(self):
        with self.assertRaises(ArgurmentError):
            FizzBuzz.isFizzOrBuzz(0)
