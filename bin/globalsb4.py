import discord
from discord.ext import commands
import re
import datetime
import sys
import os
import time
from datetime import date
from datetime import *
import math
import random
from decimal import *
from colored import fore, back, style, fg, bg, attr
from pathlib import Path
import string
import traceback
from discord.ext import commands
from math import *
import asyncio
import codecs

from DPNVT import *
from DPNGourmet import *

#TODO: Make this do something useful.
class DigiException(Exception):
    pass

#Version.
version = "0.0.1"

#Defaults
defaultheight =
defaultweight =
defaultdensity = Decimal(1.0)

#Constants.
newline = "\n"
monikalines = ["What? I don't know anyone named Monika.",
"I don't know anyone named Monika! hehheh...",
"Hey wha-- er...", "Did someone say my n- um... Monika? Weird.",
"I hear Monika was the best character in Doki Doki. I may be a bit biased though 'cause... never mind.",
"Monika? :sweat_smile: Never heard of her."]
folder = ".."
sizebot_id = #TODO: Get SB4's ID.
digiid = 271803699095928832

#Hex code stuff.
def regenhexcode():
    #16-char hex string gen for unregister.
    hexdigits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f"]
    lst = [random.choice(hexdigits) for n in range(16)]
    hexstring = "".join(lst)
    hexfile = open("hexstring.txt", "r+")
    hexfile.write(hexstring)
    hexfile.close()

def readhexcode():
    #Read the hexcode from the file.
    hexfile = open("hexstring.txt", "r+")
    hexcode = hexfile.readlines()
    hexfile.close()
    return str(hexcode[0])

#Configure decimal module.
getcontext()
context = Context(prec=100, rounding=ROUND_HALF_EVEN, Emin=-9999999, Emax=999999,
        capitals=1, clamp=0, flags=[], traps=[Overflow, DivisionByZero,
        InvalidOperation])
setcontext(context)

#Get number from string.
def getnum(string):
    numberarray = [str(s) for s in re.findall(r'\d+\.?\d*', string)]
    return Decimal(numberarray[0])

#Get letters from string.
def getlet(string):
    letterarray = [str(s) for s in re.findall(r'[a-zA-Z]+', string)]
    return letterarray[0]

#Remove trailing zeros.
#TODO
def removetrailing0s():
    pass

#Return a number rounded to the nearest .5.
def round_nearest_half(number):
    return round(number * 2) / 2

#Return a number formated with commas.
def place_value(number):
    return ("{:,}".format(number))
