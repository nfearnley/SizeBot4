import random

from discord.ext import commands

from DPNGourmet import warn


# Commands for roleplaying
class RPCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Die rolling command, XdY format
    @commands.command()
    async def roll(self, ctx, dice):
        await ctx.message.delete()
        # Check to make sure the user used XdY notation
        try:
            rolls, limit = map(int, dice.split("d"))
        except Exception:
            await ctx.send("Format has to be in XdY.")
            return
        if rolls > 100:
            # Don't let them roll a ton of dice
            await ctx.send("Too many dice! Try again.")
            print(warn(f"User {ctx.message.author.name} tried to roll {rolls} dice."))
            return
        if limit > 1000:
            # Keep number of sides rational
            await ctx.send("Dice too big! Try again.")
            print(warn(f"User {ctx.message.author.name} tried to roll a {limit}-sided dice."))
            return

        # Prettify the individual roll list
        result = ", ".join(str(random.randint(1, limit)) for r in range(rolls))
        resultarray = result.split(", ")

        # Tabulate total
        total = 0
        for x in resultarray:
            total = total + int(x)

        # Output the results to chat
        await ctx.send(
            f"<@{ctx.message.author.id}> rolled {dice}!\n"
            f"Result(s): {result}\n"
            f"Total: {total}")


# Necessary
def setup(bot):
    bot.add_cog(RPCog(bot))
