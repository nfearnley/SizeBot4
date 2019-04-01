import discord
from discord.ext import commands
from globalsb4 import *

class ModCog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, what:str = None):
        await ctx.message.delete()
        if what is None:
            await ctx.send("""<@{0}>, **Help Topics**
    note: [] indicates a required parameter, <> indicates an optional parameter.
    __*Commands*__
    ```
    register [nickname] [Y/N] [current height] [base height] [base weight] [U/M] <species>
    unregister
    roll XdY
    sing [string]```

    *Other Topics*
    ```
    about
    bug```""".format(ctx.message.author.id))

    @commands.command()
    async def about(self, ctx):
        await ctx.message.delete()
        await ctx.send("```" + ascii + "```")
        await ctx.send("""<@{0}>
    ***SizeBot4 by DigiDuncan***
    *A big program for big people.*
    **Written for the Size Matters server**
    **Additional equations** *by Benyovski and Arceus3251*
    **Alpha Tested** *by AWK_*
    **written in** *Python 3.7 with discord.py*
    **written with** Atom
    **Special thanks** *to the discord.py Community Discord for helping with code*
    **Special thanks** to the {1} users of SizeBot4.

    "She (*SizeBot*) is beautiful." -- *GoddessArete*
    ":100::thumbsup:" -- *Anonymous*
    "I am the only person who has accidentally turned my fetish into a tech support job." -- *DigiDuncan*

    Version {2} | 04 Apr 2018""".format(ctx.message.author.id, members, version))

    @commands.command()
    async def bug(self, ctx, *, message : str):
        await bot.get_user(digiid).send("<@{0}>: {1}".format(ctx.message.author.id, message))

#Necessary.
def setup(bot):
    bot.add_cog(ModCog(bot))
