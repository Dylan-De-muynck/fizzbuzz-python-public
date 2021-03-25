from fizzbuzz import *
import random

end = False
AliceRange = random.randrange(1, 9999)
AliceStart = True

print("#############################################")
print("################# FIZZBUZZ ##################")
print("#############################################")
print("")

try:
    while end == False:

        if (AliceStart == True):
            print("Alice commence avec : " + str(AliceRange))
            print("Bob répond : " + str(FizzBuzz.isFizzOrBuzz(int(AliceRange))))
            AliceStart = False

        nb = input("Alice continue avec : ")          
        print("Bob répond : " + str(FizzBuzz.isFizzOrBuzz(int(nb))))
except ArgurmentError() as e:
    print("Valeur incorrecte")