class FizzBuzz():
    @staticmethod
    def isFizzOrBuzz(nb):
        if nb <= 0:
            raise(ArgurmentError())
        if nb % 3 == 0:
            return "Fizz"



class ArgurmentError(Exception):
    def __init__(self):
        super()