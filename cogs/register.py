from globalsb4 import *

class RegisterCog:
    def __init__(self, bot):
        self.bot = bot

    #TODO: Make this a step-by-step process
    @commands.command()
    async def register(ctx, nick:str, display:str, currentheight:str,
        baseheight:str, baseweight:str, units:str, species:str = None):
        #Registers a user for SizeBot.

        #Extract values and units.
        chu = getlet(currentheight)
        bhu = getlet(baseheight)
        bwu = getlet(baseweight)
        currentheight = getnum(currentheight)
        baseheight = getnum(baseheight)
        baseweight = getnum(baseweight)

        #Convert floats to decimals.
        currentheight = Decimal(currentheight)
        baseheight = Decimal(baseheight)
        baseweight = Decimal(baseweight)

        readable = "CH {0}, CHU {1}, BH {2}, BHU {3}, BW {4}, BWU {5}".format(currentheight, chu,
            baseheight, bhu, baseweight, bwu)
        print("Nickname: {0}, Display: {1}".format(nick, display))
        print(readable)

        #Already registered.
        if os.path.exists(folder + '/users/' + str(ctx.message.author.id) + '.txt'):
            await ctx.send("""Sorry! You already registered with SizeBot.
    To unregister, use the `&unregister` command.""", delete_after=5)
            print(warn("Error UAE1 on user registration: {1}.".format(ctx.message.author)))
            return
        #Invalid size value.
        elif (currentheight <= 0 or
            baseheight <= 0 or
            baseweight <= 0):
            print(warn("Invalid size value."))
            await ctx.send("All values must be an integer greater than zero.", delete_after=3)
            return
        #Invalid display value.
        elif display.lower() not in ["y", "n"]:
            print(warn("display was {0}, must be Y or N.".format(display)))
            return
        elif units.lower() not in ["m", "u"]:
            print(warn("units was {0}, must be M or U.".format(units)))
            await ctx.send("Units must be `M` or `U`.", delete_after=3)
            return
        #Success.
        else:
            if species == None:
                species = "None"
            #Make an array of string items, one per line.
            with open(folder + '/users/' + str(ctx.message.author.id) + '.txt', "w+") as userfile:
                writethis = [str(nick) + newline, str(display) + newline, str(toSV(currentheight, chu)) +
                    newline, str(toSV(baseheight, bhu)) + newline, str(toWV(baseweight, bwu)) + newline, "1.0"
                    + newline, units + newline, species + newline]
                userfile.writelines(writethis)
                print(warn("Made a new user: {0}!").format(ctx.message.author))
                print(writethis)
                print(userfile.readlines())
            await ctx.send("Registered <@{0}>. {1}.".format(ctx.message.author.id, readable), delete_after=3)

    @register.error
    async def register_handler(ctx, error):
        # Check if required argument is missing.
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("""Not enough variables for `register`.
    Use `&register [nick] [display (Y/N)] [currentheight] [baseheight] [baseweight] [M/U]`.""", delete_after=5)

    @commands.command()
    async def unregister(ctx, code = None):
        if not os.path.exists(folder + '/users/' + str(ctx.message.author.id) + '.txt'):
        #User file missing.
            await ctx.send("""Sorry! You aren't registered with SizeBot.
    To register, use the `&register` command.""", delete_after=5)
        elif code is None:
            regenhexcode()
            await ctx.send("""To unregister, use the `&unregister` command and the following code.
    `{0}`""".format(readhexcode())
                , delete_after=5)
        elif code != readhexcode():
            await ctx.send("Incorrect code. You said: `{0}`. The correct code was: `{1}`. Try again.".format(
                code, readhexcode()), delete_after=5)
        else:
            await ctx.send("Correct code! Unregisted {0}".format(ctx.message.author.name), delete_after=3)
            os.remove(folder + "/users/" + str(ctx.message.author.id) + ".txt")

#Necessary.
def setup(bot):
    bot.add_cog(RegisterCog(bot))
