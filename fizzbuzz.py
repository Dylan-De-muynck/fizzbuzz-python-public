class FizzBuzz():
    @staticmethod
    def isFizzOrBuzz(nb):
        if nb <= 0:
            raise(ArgurmentError())
        if nb == 6:
            return "Fizz"



class ArgurmentError(Exception):
    def __init__(self):
        super()