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
"ℓₚ" : 0.00000000000000000000000000000000001616229,

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
"tn" : 907.185,

#Small SI areas
"m²" : 1,
"cm²" : 0.0001,
"mm²" : 0.000001,
"um²" : 0.000000000001,
"nm²" : 0.000000000000000001,
"pm²" : 0.000000000000000000000001,
"fm²" : 0.000000000000000000000000000001,
"am²" : 0.000000000000000000000000000000000001,
"zm²" : 0.000000000000000000000000000000000000000001,
"ym²" : 0.000000000000000000000000000000000000000000000001,
#Big SI areas.
"km²" : 1000000,
"Mm²" : 1000000000000,
"Gm²" : 1000000000000000000,
"Tm²" : 1000000000000000000000000,
"Pm²" : 1000000000000000000000000000000,
"Em²" : 1000000000000000000000000000000000000,
"Zm²" : 1000000000000000000000000000000000000000000,
"Ym²" : 1000000000000000000000000000000000000000000000000,
#US areas.
"ft²" : 0.0929,
"in²" : 0.00064516,
"yd²" : 0.8361,
"mi²" : 2590000,
"ly²" : 89510000000000000000000000000000,
"au²" : 22380000000000000000000,
"ℓₚ²" : 0.0000000000000000000000000000000000000000000000000000000000000000000002612
}

unitnames = {
#Small SI lengths.
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
"ft" : ["feet", "foot"],
"in" : ["inches", "inch"],
"yd" : ["yard"],
"mi" : ["mile"],
"ly" : ["lightyear"],
"au" : ["astronomicalunit"],
"ℓₚ" : ["plancklength", "planck", "pl", "lp"],
#Small SI weights.
"g" : ["gram"],
"mg" : ["milligram"],
"ug" : ["microgram", "μg"],
"ng" : ["nanogram"],
"pg" : ["picogram"],
"fg" : ["femtogram"],
"ag" : ["attogram"],
"zg" : ["zeptogram"],
"yg" : ["yoctogram"],
#Big SI weights.
"kg" : ["kilogram"],
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
"rice" ["rice", "grainofrice", "grain", "ricegrain"],
"oz" : ["ounce"],
"lb" : ["pound"],
"tn" : ["ton", "shortton", "USton"],
#Small SI areas.
"m²" : ["meter²", "metre²", "meter2", "metre2", "squaremeter", "squaremetre"],
"cm²" : ["centimeter²", "centimetre²", "centimeter2", "centimetre2", "squarecentimeter", "squarecentimetre"],
"mm²" : ["millimeter²", "millimetre²", "millimeter2", "millimetre2", "squaremillimeter", "squaremillimetre"],
"um²" : ["micrometer²", "micrometre²", "micron²", "μm²", "micrometer2", "micrometre2", "micron2", "μm2", "squaremicrometer", "squaremicrometre", " squaremicron", "squareμm"],
"nm²" : ["nanometer²", "nanometre²", "nanometer2", "nanometre2", "squarenanometer", "squarenanometre"],
"pm²" : ["picometer²", "picometere²", "picometer2", "picometere2", "squarepicometer", "squarepicometere"],
"fm²" : ["femtometer²", "femotmetre²", "femtometer2", "femotmetre2", "squarefemtometer", "squarefemotmetre"],
"am²" : ["attometer²", "attometre²", "attometer2", "attometre2", "squareattometer", "squareattometre"],
"zm²" : ["zeptometer²", "zeptometre²", "zeptometer2", "zeptometre2", "squarezeptometer", "squarezeptometre"],
"ym²" : ["yoctometer²", "yoctometre²", "yoctometer2", "yoctometre2", "squareyoctometer", "squareyoctometre"],
#Big SI areas.
"km²" : ["kilometer²", "kilometre²", "kilometer2", "kilometre2", "squarekilometer", "squarekilometre"],
"Mm²" : ["megameter²", "megametre²", "megameter2", "megametre2", "squaremegameter", "squaremegametre"],
"Gm²" : ["gigameter²", "gigametre²", "gigameter2", "gigametre2", "squaregigameter", "squaregigametre"],
"Tm²" : ["terameter²", "terametre²", "terameter2", "terametre2", "squareterameter", "squareterametre"],
"Pm²" : ["petameter²", "petametre²", "petameter2", "petametre2", "squarepetameter", "squarepetametre"],
"Em²" : ["exameter²", "exametre²", "exameter2", "exametre2", "squareexameter", "squareexametre"],
"Zm²" : ["zettameter²", "zettametre²", "zettameter2", "zettametre2", "squarezettameter", "squarezettametre"],
"Ym²" : ["yottameter²", "yottametre²", "yottameter2", "yottametre2", "squareyottameter", "squareyottametre"],
#US areas.
"ft²" : ["feet²", "foot²", "feet2", "foot2", "squarefeet", "squarefoot"],
"in²" : ["inches²", "inch²", "inches2", "inch2", "squareinches", "squareinch"],
"yd²" : ["yard²", "yard2", "squareyard"],
"mi²" : ["mile²", "mile2", "squaremile"],
"ly²" : ["lightyear²", "lightyear2", "squarelightyear"],
"au²" : ["astronomicalunit²", "astronomicalunit2", "squareastronomicalunit"],
"ℓₚ²" : ["plancklength²", "planck²", "pl²", "lp²", "plancklength2", "planck2", "pl2", "lp2", "squareplancklength", "squareplanck", "squarepl", "squarelp"],
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
# Remove spaces before check against the unitnames.
def convertname(fullname):
    pass
