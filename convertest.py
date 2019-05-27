from digiconvert import *
from globalsb4 import *

fromstuff = input("Input a \'from\' value and measurement. > ")
tomeasure = input("To what measurement? > ")

fromvalue = getnum(fromstuff)
frommeasure = getlet(fromstuff)

print()

convert(fromvalue, frommeasure, tomeasure)

print()
