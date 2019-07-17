from discord.ext import commands

from sizebot4 import conf
from sizebot4.globalsb4 import version


class ModCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, what: str = None):
        await ctx.message.delete()
        # TODO: Add support for multiple commands
        if what is None:
            await ctx.send(
                f"<@{ctx.message.author.id}>, **Help Topics**\n"
                "note: [] indicates a required parameter, <> indicates an optional parameter.\n"
                "__*Commands*__\n"
                "```\n"
                "register [nickname] [Y/N] [current height] [base height] [base weight] [U/M] <species>\n"
                "unregister\n"
                "roll XdY\n"
                "sing [string]```\n"
                "\n"
                "*Other Topics*\n"
                "```\n"
                "about\n"
                "bug```")

    @commands.command()
    async def about(self, ctx):
        member_count = "many"  # TODO: Change this to get the number of users in the sizebot database
        await ctx.message.delete()
        await ctx.send(f"```{conf.banner}```")
        await ctx.send(
            f"<@{ctx.message.author.id}>\n"
            "***SizeBot4 by DigiDuncan***\n"
            "*A big program for big people.*\n"
            "**Written for the Size Matters server**\n"
            "**Additional equations** *by Benyovski and Arceus3251*\n"
            "**Alpha Tested** *by AWK_*\n"
            "**written in** *Python 3.7 with discord.py*\n"
            "**written with** Atom\n"
            "**Special thanks** *to the discord.py Community Discord for helping with code*\n"
            f"**Special thanks** to the {member_count} users of SizeBot4.\n"
            "\n"
            '"She (*SizeBot*) is beautiful." -- *GoddessArete*\n'
            '":100::thumbsup:" -- *Anonymous*\n'
            '"I am the only person who has accidentally turned my fetish into a tech support job." -- *DigiDuncan*\n'
            "\n"
            f"Version {version} | 04 Apr 2018")

    @commands.command()
    async def bug(self, ctx, *, message: str):
        await self.bot.get_user(conf.owner_id).send(f"<@{ctx.message.author.id}>: {message}")


# Necessary
def setup(bot):
    bot.add_cog(ModCog(bot))
