from digiconvert import *
print()
print("'Full Name > Unit' test")
test1 = ["meters", "kilometre", "astronomical unit", "light years"]

for test in test1:
    print(test + " | " + convertname(test))

print()
print("'Convert' test")

convert(9, "meters", "centimeters")
convert(5, "inches", "centimeters")
convert(10, "yards", "meters")
convert(115, "lb", "kilograms")
convert(50, "kg", "pounds")
convert(7, "'", "inch")
print()
