import os
from decimal import Decimal
import sys
import traceback

from discord.ext import commands

from DPNGourmet import warn
from globalsb4 import regenhexcode, readhexcode, getnum, getlet, folder
import digidatabase as db

class RegisterCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # TO DO: Make this a step-by-step process
    @commands.command()
    async def register(self, ctx, nick:str, display:str, currentheight:str,
        baseheight:str, baseweight:str, units:str, species:str="None"):
        # Registers a user for SizeBot.

        # Extract values and units.
        chu = getlet(currentheight)
        bhu = getlet(baseheight)
        bwu = getlet(baseweight)
        currentheight = getnum(currentheight)
        baseheight = getnum(baseheight)
        baseweight = getnum(baseweight)

        # Convert floats to decimals.
        currentheight = Decimal(currentheight)
        baseheight = Decimal(baseheight)
        baseweight = Decimal(baseweight)

        readable = "CH {0}, CHU {1}, BH {2}, BHU {3}, BW {4}, BWU {5}".format(currentheight, chu,
                                                                              baseheight, bhu,
                                                                              baseweight, bwu)
        print("Nickname: {0}, Display: {1}".format(nick, display))
        print(readable)

        # Already registered.
        if db.userFileExists(ctx.message.author.id):
            await ctx.send("Sorry! You already registered with SizeBot.\n"
                           "To unregister, use the `&unregister` command.",
                delete_after=5)
            print(warn("Error UAE1 on user registration: {0}.".format(ctx.message.author)))
            return

        # Invalid size value.
        if (currentheight <= 0 or baseheight <= 0 or baseweight <= 0):
            print(warn("Invalid size value."))
            await ctx.send("All values must be an integer greater than zero.", delete_after=3)
            return

        # Invalid display value.
        if display.lower() not in ["y", "n"]:
            print(warn("display was {0}, must be Y or N.".format(display)))
            return
        
        # Invalid units value.
        if units.lower() not in ["m", "u"]:
            print(warn("units was {0}, must be M or U.".format(units)))
            await ctx.send("Units must be `M` or `U`.", delete_after=3)
            return

        # Success.
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
            "species": species
        }
        db.saveUserFile(ctx.message.author, data)
        await ctx.send("Registered <@{}>. {}.".format(ctx.message.author.id, readable),
                        delete_after=3)

    @register.error
    async def register_handler(self, ctx, error):
        # Check if required argument is missing.
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Not enough variables for `register`.\n"
                           "Use `&register [nick] [display (Y/N)] [currentheight] [baseheight] [baseweight] [M/U]`.",
                           delete_after=5)
            return

        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

    # TO DO: Change this to use YES/NO emojis, instead of a hexcode
    @commands.command()
    async def unregister(self, ctx, code=None):
        # User is not registered
        if not db.userFileExists(ctx.message.author.id):
            await ctx.send("Sorry! You aren't registered with SizeBot.\n"
                           "To register, use the `&register` command.", 
                           delete_after=5)
            return

        # User didn't enter a hexcode
        if code is None:
            hexcode = regenhexcode()
            await ctx.send(("To unregister, use the `&unregister` command and the following code.\n"
                            "`{0}`").format(hexcode),
                           delete_after=5)
            return
        
        # User entered the wrong hexcode
        if code != readhexcode():
            await ctx.send("Incorrect code. You said: `{0}`. The correct code was: `{1}`. Try again.".format(code, readhexcode()),
                           delete_after=5)
            return

        # User successfully unregistered
        await ctx.send("Correct code! Unregistered {0}".format(ctx.message.author.name),
                       delete_after=3)
        db.deleteUserFile(ctx.message.author.id)

# Necessary.
def setup(bot):
    bot.add_cog(RegisterCog(bot))
