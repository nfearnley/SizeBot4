#Oh god, here we go.
#DigiConvert is a "package" for converting units to other units,
#Mainly because I don't like any other unit conversion packages.
#For now it's just going to be units the SizeBot uses but maybe I'll add more and make this public later.

from globalsb4 import *

#NOTE: A VUpair is a [Decimal/float, string] pair, where the first variable is the
#value, and the second variable is the unit. SizeBot will be taking in and
#outputting these where possible, for consistency.

#Custom exceptions.
class UnitTypeMismatchError(Exception):
	pass
class UnitNotFoundError(Exception):
	pass

#All multipliers are based on the SI unit for that unit type.
#So, meters, kilograms, square meters.
#Each key is its abbreviation.
unitmultipliers = {
"length" : {
#Small SI lengths
"ℓₚ" : 0.00000000000000000000000000000000001616229,
"ym" : 0.000000000000000000000001,
"zm" : 0.000000000000000000001,
"am" : 0.000000000000000001,
"fm" : 0.000000000000001,
"pm" : 0.000000000001,
"nm" : 0.000000001,
"μm" : 0.000001,
"mm" : 0.001,
"cm" : 0.01,
#Big SI lengths.
"m" : 1,
"km" : 1000,
"Mm" : 1000000,
"Gm" : 1000000000,
"Tm" : 1000000000000,
"Pm" : 1000000000000000,
"Em" : 1000000000000000000,
"Zm" : 1000000000000000000000,
"Ym" : 1000000000000000000000000,
"uni" : 880000000000000000000000000,
#US lengths.
"in" : 0.0254,
"ft" : 0.3048,
"yd" : 0.9144,
"mi" : 1609.34,
"au" : 149597870700,
"ly" : 9460730472580800,
#Astronomical object lengths.
"🌎" : 12742020,
"☀️" : 1391000000,
"🌌" : 946073047258080000000,
},
"weight" : {
#Small SI weights.
"yg" : 0.000000000000000000000000001,
"zg" : 0.000000000000000000000001,
"ag" : 0.000000000000000000001,
"fg" : 0.000000000000000001,
"pg" : 0.000000000000001,
"ng" : 0.000000000001,
"μg" : 0.000000001,
"mg" : 0.000001,
"g" : 0.001,
#Big SI weights.
"kg" : 1,
"st" : 6.35029,
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
"tn" : 907.185,
#TODO: Add astronomical weights.
"🌎w" : 5972000000000000000000000,
"☀️w" : 1988435000000000000000000000000000,
"🌌w" : 1988435000000000000000000000000000 * 480000000000,
"uniw": 200000000000000000000000000000000000000000000000000000
},
"area" : {
#Small SI areas
"ym²" : 0.000000000000000000000000000000000000000000000001,
"zm²" : 0.000000000000000000000000000000000000000001,
"am²" : 0.000000000000000000000000000000000001,
"fm²" : 0.000000000000000000000000000001,
"pm²" : 0.000000000000000000000001,
"nm²" : 0.000000000000000001,
"μm²" : 0.000000000001,
"mm²" : 0.000001,
"cm²" : 0.0001,
#Big SI areas.
"m²" : 1,
"km²" : 1000000,
"Mm²" : 1000000000000,
"Gm²" : 1000000000000000000,
"Tm²" : 1000000000000000000000000,
"Pm²" : 1000000000000000000000000000000,
"Em²" : 1000000000000000000000000000000000000,
"Zm²" : 1000000000000000000000000000000000000000000,
"Ym²" : 1000000000000000000000000000000000000000000000000,
#US areas.
"ℓₚ²" : 0.0000000000000000000000000000000000000000000000000000000000000000000002612,
"in²" : 0.00064516,
"ft²" : 0.0929,
"yd²" : 0.8361,
"mi²" : 2590000,
"au²" : 22380000000000000000000,
"ly²" : 89510000000000000000000000000000
}
}

unitnames = {
#Small SI lengths.
"m" : ["meter", "metre"],
"cm" : ["centimeter", "centimetre"],
"mm" : ["millimeter", "millimetre"],
"μm" : ["micrometer", "micrometre", "micron", "um"],
"nm" : ["nanometer", "manometre"],
"pm" : ["picometer", "picometere"],
"fm" : ["femtometer", "femotmetre"],
"am" : ["attometer", "attometre"],
"zm" : ["zeptometer", "zeptometre"],
"ym" : ["yoctometer", "yoctometre"],
#Big SI lengths
"km" : ["kilometer", "kilometre"],
"Mm" : ["megameter", "megametre"],
"Gm" : ["gigameter", "gigametre"],
"Tm" : ["terameter", "terametre"],
"Pm" : ["petameter", "petametre"],
"Em" : ["exameter", "exametre"],
"Zm" : ["zettameter", "zettametre"],
"Ym" : ["yottameter", "yottametre"],
#US lengths.
"ft" : ["feet", "foot", "\'"],
"in" : ["inches", "inch", "\""],
"yd" : ["yard"],
"mi" : ["mile"],
"ly" : ["lightyear"],
"au" : ["astronomicalunit"],
"ℓₚ" : ["plancklength", "planck", "pl", "lp"],
#Astronomical objects lengths.
"🌎" : ["earth"],
"☀️" : ["sun"],
"🌌" : ["galaxy", "galaxies", "milkyway"],
"uni" : ["universe", "observableuniverse", "ouni"],
#Small SI weights.
"g" : ["gram"],
"mg" : ["milligram"],
"μg" : ["microgram", "ug"],
"ng" : ["nanogram"],
"pg" : ["picogram"],
"fg" : ["femtogram"],
"ag" : ["attogram"],
"zg" : ["zeptogram"],
"yg" : ["yoctogram"],
#Big SI weights.
"kg" : ["kilogram"],
"st" : ["stone"],
"t" : ["tonne", "metricton", "metrictonne"],
"kt" : ["kiloton", "metrickiloton", "kilotonne", "metrickilotonen"],
"Mt" : ["megaton", "metricmegaton", "megatonne", "metricmegatonne"],
"Gt" : ["gigaton", "metricgigaton", "gigatonne", "metricgigatonne"],
"Tt" : ["teraton", "metricteraton", "teratonne", "metricteratonne"],
"Pt" : ["petaton", "metricpetaton", "petatonne", "metricpetatonne"],
"Et" : ["exaton", "metricexaton", "exatonne", "metricexatonne"],
"Zt" : ["zettaton", "metriczettaton", "zettatonne", "metriczettatonne"],
"Yt" : ["yottaton", "metricyottaton", "yottatonne", "metricyottatonne"],
#US weights.
"rice" : ["rice", "grainofrice", "grain", "ricegrain"],
"oz" : ["ounce"],
"lb" : ["pound"],
"tn" : ["ton", "shortton", "USton"],
#Astronomical objects weights.
"🌎w" : ["earthw", "earthweight"],
"☀️w" : ["sunw, sunweight"],
"🌌w" : ["galaxyw", "galaxiesw", "milkywayw", "galaxyweight", "galaxiesweight", "milkywayweight", "milkywight"],
"uniw" : ["universew", "observableuniversew", "ouniw", "universeweight", "observableuniverseweight", "ouniweight"],
#Small SI areas.
"m²" : ["meter²", "metre²", "meter2", "metre2", "squaremeter", "squaremetre", "sqm"],
"cm²" : ["centimeter²", "centimetre²", "centimeter2", "centimetre2", "squarecentimeter", "squarecentimetre", "sqcm"],
"mm²" : ["millimeter²", "millimetre²", "millimeter2", "millimetre2", "squaremillimeter", "squaremillimetre", "sqmm"],
"μm²" : ["micrometer²", "micrometre²", "micron²", "um²", "micrometer2", "micrometre2", "micron2", "um2", "squaremicrometer", "squaremicrometre", " squaremicron", "squareum", "sqμm"],
"nm²" : ["nanometer²", "nanometre²", "nanometer2", "nanometre2", "squarenanometer", "squarenanometre", "sqnm"],
"pm²" : ["picometer²", "picometere²", "picometer2", "picometere2", "squarepicometer", "squarepicometere", "sqpm"],
"fm²" : ["femtometer²", "femotmetre²", "femtometer2", "femotmetre2", "squarefemtometer", "squarefemotmetre", "sqfm"],
"am²" : ["attometer²", "attometre²", "attometer2", "attometre2", "squareattometer", "squareattometre", "sqam"],
"zm²" : ["zeptometer²", "zeptometre²", "zeptometer2", "zeptometre2", "squarezeptometer", "squarezeptometre", "sqzm"],
"ym²" : ["yoctometer²", "yoctometre²", "yoctometer2", "yoctometre2", "squareyoctometer", "squareyoctometre", "sqym"],
#Big SI areas.
"km²" : ["kilometer²", "kilometre²", "kilometer2", "kilometre2", "squarekilometer", "squarekilometre", "sqkm"],
"Mm²" : ["megameter²", "megametre²", "megameter2", "megametre2", "squaremegameter", "squaremegametre"],
"Gm²" : ["gigameter²", "gigametre²", "gigameter2", "gigametre2", "squaregigameter", "squaregigametre", "sqgm"],
"Tm²" : ["terameter²", "terametre²", "terameter2", "terametre2", "squareterameter", "squareterametre", "sqtm"],
"Pm²" : ["petameter²", "petametre²", "petameter2", "petametre2", "squarepetameter", "squarepetametre"],
"Em²" : ["exameter²", "exametre²", "exameter2", "exametre2", "squareexameter", "squareexametre", "sqem"],
"Zm²" : ["zettameter²", "zettametre²", "zettameter2", "zettametre2", "squarezettameter", "squarezettametre"],
"Ym²" : ["yottameter²", "yottametre²", "yottameter2", "yottametre2", "squareyottameter", "squareyottametre"],
#US areas.
"ft²" : ["feet²", "foot²", "feet2", "foot2", "squarefeet", "squarefoot", "sqft"],
"in²" : ["inches²", "inch²", "inches2", "inch2", "squareinches", "squareinch", "sqin"],
"yd²" : ["yard²", "yard2", "squareyard", "sqyd"],
"mi²" : ["mile²", "mile2", "squaremile", "sqmi"],
"ly²" : ["lightyear²", "lightyear2", "squarelightyear", "sqly"],
"au²" : ["astronomicalunit²", "astronomicalunit2", "squareastronomicalunit", "sqau"],
"ℓₚ²" : ["plancklength²", "planck²", "pl²", "lp²", "plancklength2", "planck2", "pl2", "lp2", "squareplancklength", "squareplanck", "squarepl", "squarelp", "sqℓₚ", "sqlp", "sqpl"],
}

#Different scales and their cutoffs )for display only.)
#If the size given is above the key, it will use the value of that pair as it's convert-to unit.
#TODO: Not done.
orders = {
metriclength : {
0: "ℓₚ",
0.000000000000000000000001: "ym",
0.000000000000000000001: "zm",
0.000000000000000001 : "am",
0.000000000000001 : "fm",
0.000000000001: "pm",
0.000000001: "nm",
0.000001: "μm",
0.0001: "mm", #Intentionally incorrect value, shows mm starting at 0.1mm.
0.01: "cm",
1: "m",
1000: "km",
1000000: "Mm",
1000000000: "Gm",
1000000000000: "Tm",
1000000000000000: "Pm",
1000000000000000000: "Em",
1000000000000000000000: "Zm",
1000000000000000000000000: "Ym",
880000000000000000000000000: "uni"
},
uslength : {
0: "ℓₚ",
0.000000000000000000000001: "ym",
0.000000000000000000001: "zm",
0.000000000000000001 : "am",
0.000000000000001 : "fm",
0.000000000001: "pm",
0.000000001: "nm",
0.000001: "μm",
0.0254 : "in",
0.3048 : "ft",
1609.34 : "mi", #Yard intentionally skipped.
12742020: "🌎",
1391000000: "☀️",
946073047258080000000: "🌌",
880000000000000000000000000: "uni"
}
}

def toShoeSize(VUpair):
	inchamount = convert(VUpair, "in")[0]
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

#eg: convertName("meter") > returns "m"
# Auto test without 's' at the end of a unit.
# Removes spaces and lower() before check against the unitnames.
def convertName(fullname):
	fullname = fullname.lower()
	fullname = fullname.replace(" ", "")
	fullnameplural = fullname[:-1]
	for unit, names in unitnames.items():
		if fullname in names or fullnameplural in names:
			return unit
	return fullname

#eg: findreasonableunit([5000, "meter"], "length", "metric") > "km"
#For user-end display. (Size tags, stats...)
#Uses orders{}.
def findReasonableUnit(VUpair, unittype, system):
	pass

def isFeetAndInchesAndIfSoFixIt(input):
	if re.search(r"([0-9.]+)(\'|ft)([0-9.]+)(\"|in)", input):
		print("Feet and inches...")
		m = re.match(r"([0-9.]+)(\'|ft)([0-9.]+)(\"|in)", input)
		feet = Decimal(m.group(1))
		inch = Decimal(m.group(3))
		totalinches = (feet * 12) + inch
		return f"{totalinches}in"
	else:
		return input

#Return a VUpair.
def convert(VUpair, unitto):
	#Set up our variables.
	VUpair[0] = amount
	VUpair[1] = unitfrom
	unitfromKey = convertName(unitfrom)
	unittoKey = convertName(unitto)
	frommult = 0
	tomult = 0
	unittype = None

	#Test to see the unit type.
	if unitfromKey in unitmultipliers["length"]: unittype = "length"
	if unitfromKey in unitmultipliers["weight"]: unittype = "weight"
	if unitfromKey in unitmultipliers["area"]: unittype = "area"

	#If the unit's not there, we throw an error.
	if unittype = None: raise UnitNotFoundError

	#Test if the to unit exists and matches type.
	if unittoKey not in unitmultipliers[unittype]: raise UnitTypeMismatchError

	#Get the multipliers based on their key.
	for nestedname, nesteddict in unitmultipliers.items():
		if unitfromKey in nesteddict.keys():
			frommult = nesteddict[unitfromKey]
	for nestedname, nesteddict in unitmultipliers.items():
		if unittoKey in nesteddict.keys():
			tomult = nesteddict[unittoKey]

	#Do the math.
	newamount = Decimal(amount) * Decimal(frommult) / Decimal(tomult)
	newamount = round(newamount, 3)

	#Return a VUpair.
	print(f"convert(amount: {amount}, unitfrom: {unitfrom}, unitto: {unitto})")
	print(f"{amount}{unitfromKey} | {newamount}{unittoKey}")
	print()
	return [newamount, unittoKey]
