from globalsb4 import getnum, getlet

print()

fromstuff = input("Input a \'from\' value and measurement. > ")
tomeasure = input("To what measurement? > ")

fromstuff = isFeetAndInchesAndIfSoFixIt(fromstuff)

fromvalue = getnum(fromstuff)
frommeasure = getlet(fromstuff)

print()

convert(fromvalue, frommeasure, tomeasure)

print()
