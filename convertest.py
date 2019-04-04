from digiconvert import *

test1 = ["meters", "kilometre", "astronomical unit", "light years"]

for test in test1:
    print(test + " | " + convertname(test))
