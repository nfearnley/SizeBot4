#Oh god, here we go.
#DigiConvert is a "package" for converting units to other units,
#Mainly because I don't like any other unit conversion packages.
#For now it's just going to be units the SizeBot uses but maybe I'll add more and make this public later.

#All multipliers are based on the SI unit for that unti type.
#So, meters, kilograms, square meters.
#Each key is it's abbreviation.
unitmultipliers = {
#Small SI lengths
"m" : 1,
"cm" : 0.01,
"mm" : 0.001,
"um" : 0.000001,
"nm" : 0.000000001,
"pm" : 0.000000000001,
"fm" : 0.000000000000001,
"am" : 0.000000000000000001,
"zm" : 0.000000000000000000001,
"ym" : 0.000000000000000000000001,
#Big SI lengths.
"km" : 1000,
"Mm" : 1000000,
"Gm" : 1000000000,
"Tm" : 1000000000000,
"Pm" : 1000000000000000,
"Em" : 1000000000000000000,
"Zm" : 1000000000000000000000,
"Ym" : 1000000000000000000000000,
#US lengths.
"ft" : 0.3048,
"in" : 0.0254,
"yd" : 0.9144,
"mi" : 1609.34,
"ly" : 9460730472580800,
"au" : 149597870700,
"lp" : 0.00000000000000000000000000000000001616229
}

unitnames = {
"m" : ["meter", "metre"],
"cm" : ["centimeter", "centimetre"],
"mm" : ["millimeter", "millimetre"],
"um" : ["micrometer", "micrometre", "micron"],
"nm" : ["nanometer", "manometre"],
"pm" : ["picometer", "picometere"],
"fm" : ["femtometer", "femotmetre"],
"am" : ["attometer", "attometre"],
"zm" : ["zeptometer", "zeptometre"],
"ym" : ["yoctometer", "yoctometre"],
"km" : ["kilometer", "kilometre"],
"Mm" : ["megameter", "megametre"],
"Gm" : ["gigameter", "gigametre"],
"Tm" : ["terameter", "terametre"],
"Pm" : ["petameter", "petametre"],
"Em" : ["exameter", "exametre"],
"Zm" : ["zettameter", "zettametre"],
"Ym" : ["yottameter", "yottametre"],
"ft" : ["feet", "foot"],
"in" : ["inches", "inch"],
"yd" : ["yard"],
"mi" : ["mile"],
"ly" : ["lightyear", "light year"],
"au" : ["astronomical unit", "astronomicalunit"],
"lp" : ["planck length", "plancklength", "planck"]
}

def toShoeSize(inchamount):
	child = False
	inches = Decimal(inchamount)
	shoesize = 3 * inches
	shoesize = shoesize - 22
	if shoesize < 1:
		child = True
		shoesize += 12 + Decimal(1/3)
	shoesize = place_value(round_nearest_half(shoesize))
	if child == True: shoesize = "Children's " + shoesize
	return shoesize

def fromShoeSize(size):
	child = False
	if "c" in size.toLower(): child = True
	size = getnum(size)
	inches = Decimal(size) + 22
	if child == True: inches = Decimal(size) + 22 - 12 - (1/3)
	inches = inches / Decimal(3)
	out = inches * inch
	return out

#TODO: Code this
#Return a float.
def convertunit(amount, from, to):
    pass

#TODO: Code this
#eg: convertname("meter") > returns "m"
# Auto detect 's' at the end of a unit.
def convertname(fullname):
    pass
