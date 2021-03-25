from fizzbuzz import *
import os
try:
    nb = input("Le nombre d'Alice : ")

    print("Bob dit : "+ str(FizzBuzz.isFizzOrBuzz(int(nb))))

    os.system("pause")
except ArgurmentError() as e:
    print("Valeur incorrecte")