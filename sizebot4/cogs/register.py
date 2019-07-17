import os
from decimal import Decimal
import sys
import traceback

from discord.ext import commands

from sizebot4 import logging
from sizebot4.globalsb4 import regenhexcode, readhexcode, getnum, getlet
import sizebot4.digidatabase as db


class RegisterCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # TODO: Make this a step-by-step process
    @commands.command()
    async def register(self, ctx, nick: str, display: str, currentheight: str, baseheight: str, baseweight: str, units: str, species: str = "None"):
        # Registers a user for SizeBot

        # Extract values and units
        chu = getlet(currentheight)
        bhu = getlet(baseheight)
        bwu = getlet(baseweight)
        currentheight = getnum(currentheight)
        baseheight = getnum(baseheight)
        baseweight = getnum(baseweight)

        # Convert floats to decimals
        currentheight = Decimal(currentheight)
        baseheight = Decimal(baseheight)
        baseweight = Decimal(baseweight)

        readable = f"CH {currentheight}, CHU {chu}, BH {baseheight}, BHU {bhu}, BW {baseweight}, BWU {bwu}"
        logging.log(f"Nickname: {nick}, Display: {display}", timestamp=False)
        logging.log(readable, timestamp=False)

        # Already registered
        if db.userFileExists(ctx.message.author.id):
            await ctx.send(
                "Sorry! You already registered with SizeBot.\n"
                "To unregister, use the `&unregister` command.",
                delete_after=5)
            logging.warn(f"Error UAE1 on user registration: {ctx.message.author}.")
            return

        # Invalid size value
        if currentheight <= 0 or baseheight <= 0 or baseweight <= 0:
            logging.warn("Invalid size value.")
            await ctx.send("All values must be an integer greater than zero.", delete_after=3)
            return

        # Invalid display value
        if display.lower() not in ["y", "n"]:
            logging.warn(f"display was {display}, must be Y or N.")
            return

        # Invalid units value
        if units.lower() not in ["m", "u"]:
            logging.warn(f"units was {units}, must be M or U.")
            await ctx.send("Units must be `M` or `U`.", delete_after=3)
            return

        # Success
        data = {
            "nick": nick,
            "display": display,
            "currentheight": currentheight,
            "chu": chu,
            "baseheight": baseheight,
            "bhu": bhu,
            "baseweight": baseweight,
            "bwu": bwu,
            "units": units,
            "species": species,
        }
        db.saveUserFile(ctx.message.author, data)
        await ctx.send(f"Registered <@{ctx.message.author.id}>. {readable}.", delete_after=3)

    @register.error
    async def register_handler(self, ctx, error):
        # Check if required argument is missing
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                "Not enough variables for `register`.\n"
                "Use `&register [nick] [display (Y/N)] [currentheight] [baseheight] [baseweight] [M/U]`.",
                delete_after=5)
            return

        print(f"Ignoring exception in command {ctx.command}:", file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

    # TODO: Change this to use YES/NO emojis, instead of a hexcode
    @commands.command()
    async def unregister(self, ctx, code=None):
        # User is not registered
        if not db.userFileExists(ctx.message.author.id):
            await ctx.send(
                "Sorry! You aren't registered with SizeBot.\n"
                "To register, use the `&register` command.",
                delete_after=5)
            return

        # User didn't enter a hexcode
        if code is None:
            hexcode = regenhexcode()
            await ctx.send(
                "To unregister, use the `&unregister` command and the following code.\n"
                f"`{hexcode}`",
                delete_after=5)
            return

        # User entered the wrong hexcode
        if code != readhexcode():
            await ctx.send(f"Incorrect code. You said: `{code}`. The correct code was: `{readhexcode()}`. Try again.", delete_after=5)
            return

        # User successfully unregistered
        await ctx.send(f"Correct code! Unregistered {ctx.message.author.name}", delete_after=3)
        db.deleteUserFile(ctx.message.author.id)


# Necessary
def setup(bot):
    bot.add_cog(RegisterCog(bot))
