from globalsb4 import *

#Commands for non-size stuff.
class FunCog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def say(self, ctx, *, message : str):
        await ctx.message.delete()
        if ctx.message.author.id == digiid:
            await ctx.send(message)

    @commands.command()
    async def sing(self, ctx, *, inString : str):
        await ctx.message.delete()
        newstring = ":musical_score: *" + inString + "* :musical_note:"
        await ctx.send(newstring)

#Necessary.
def setup(bot):
    bot.add_cog(FunCog(bot))
