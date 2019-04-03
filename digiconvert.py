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
"lp" : 0.00000000000000000000000000000000001616229,

#Small SI weights.
"g" : 0.001,
"mg" : 0.000001,
"ug" : 0.000000001,
"ng" : 0.000000000001,
"pg" : 0.000000000000001,
"fg" : 0.000000000000000001,
"ag" : 0.000000000000000000001,
"zg" : 0.000000000000000000000001,
"yg" : 0.000000000000000000000000001,
#Big SI weights.
"kg" : 1,
"t" : 1000,
"kt" : 1000000,
"Mt" : 1000000000,
"Gt" : 1000000000000,
"Tt" : 1000000000000000,
"Pt" : 1000000000000000000,
"Et" : 1000000000000000000000,
"Zt" : 1000000000000000000000000,
"Yt" : 1000000000000000000000000000,
#US weights.
"rice" : 0.000029,
"oz" : 0.02835,
"lb" : 0.4636,
"tn" : 907.185
}

unitnames = {
"m" : ["meter", "metre"],
"cm" : ["centimeter", "centimetre"],
"mm" : ["millimeter", "millimetre"],
"um" : ["micrometer", "micrometre", "micron", "μm"],
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
"lp" : ["planck length", "plancklength", "planck"],
"g" : ["gram"],
"mg" : ["milligram"],
"ug" : ["microgram", "μg"],
"ng" : ["nanogram"],
"pg" : ["picogram"],
"fg" : ["femtogram"],
"ag" : ["attogram"],
"zg" : ["zeptogram"],
"yg" : ["yoctogram"],
"kg" : ["kilogram"],
"t" : ["ton", "metric ton"],
"kt" : ["kiloton", "metric kiloton"],
"Mt" : ["megaton", "metric megaton"],
"Gt" : ["gigaton", "metric gigaton"],
"Tt" : ["teraton", "metric teraton"],
"Pt" : ["petaton", "metric petaton"],
"Et" : ["exaton", "metric exaton"],
"Zt" : ["zettaton", "metric zettaton"],
"Yt" : ["yottaton", "metric yottaton"],
"rice" ["rice", "grain of rice", "grain"],
"oz" : ["ounce"],
"lb" : ["pound"],
"tn" : ["ton", "short ton", "US ton"]
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
