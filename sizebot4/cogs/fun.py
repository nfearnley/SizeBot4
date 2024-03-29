from discord.ext import commands

from sizebot4 import conf

# Commands for non-size stuff


class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def say(self, ctx, *, message: str):
        await ctx.message.delete()
        if ctx.message.author.id != conf.owner_id:
            return
        await ctx.send(message)

    @commands.command()
    async def sing(self, ctx, *, inString: str):
        await ctx.message.delete()
        await ctx.send(f":musical_score: *{inString}* :musical_note:")


# Necessary
def setup(bot):
    bot.add_cog(FunCog(bot))
