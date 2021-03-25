class FizzBuzz():
    @staticmethod
    def isFizzOrBuzz(nb):
        if nb == 0:
            raise(ArgurmentError())



class ArgurmentError(Exception):
    def __init__(self):
        super()