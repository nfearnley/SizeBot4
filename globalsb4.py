import os
import re
from decimal import Decimal, Context, getcontext, setcontext, ROUND_HALF_EVEN, Overflow, DivisionByZero, InvalidOperation

import discord


# TODO: Make this do something useful
class DigiException(Exception):
    pass


# Version
version = "0.0.1"

# Defaults
defaultheight = None  # TODO: Set to the new value/unit pairs
defaultweight = None  # TODO: Set to the new value/unit pairs
defaultdensity = Decimal(1.0)

# Constants
folder = ".."
reol = 106871675617820672
sizebot_id = None  # TODO: Get SB4's ID
digiid = 271803699095928832


# Hex code stuff

# Generate a new 16-char hex string for unregister, and save it to a file
def regenhexcode():
    hexcode = os.urandom(8).hex()
    with open("hexstring.txt", "w") as hexfile:
        hexfile.write(hexcode)
    return hexcode


# Read the hexcode from the file
# If file is not accessible or invalid, then return None
def readhexcode():
    try:
        with open("hexstring.txt", "r") as hexfile:
            hexcode = hexfile.readline().strip()
            if len(hexcode) != 16:
                hexcode = None
    except IOError:
        hexcode = None
    return hexcode


# Configure decimal module
getcontext()
context = Context(prec=100, rounding=ROUND_HALF_EVEN, Emin=-9999999, Emax=999999,
                  capitals=1, clamp=0, flags=[], traps=[Overflow, DivisionByZero,
                                                        InvalidOperation])
setcontext(context)


# Get number from string
def getnum(inString):
    numberarray = [str(s) for s in re.findall(r"\d+\.?\d*", inString)]
    return Decimal(numberarray[0])


# Get letters from string
def getlet(inString):
    letterarray = [str(s) for s in re.findall(r"[a-zA-Z]+", inString)]
    return letterarray[0]


# Remove trailing zeros
# TODO: Implement
def removetrailing0s():
    # (\d*\.[123456789]*)0*
    pass


# Return a number rounded to the nearest 0.5
def round_nearest_half(number):
    return round(number * 2) / 2


# Return a number formated with commas
def place_value(number):
    return ("{:,}".format(number))


# Disable commands for users with the SizeBot_Banned role
def check(ctx):
    if not isinstance(ctx.channel, discord.abc.GuildChannel):
        return False

    role = discord.utils.get(ctx.author.roles, name="SizeBot_Banned")
    return role is None
