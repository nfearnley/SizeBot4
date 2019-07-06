import os

import discord
from discord.ext import commands
from colored import bg, fg, fore, style

from DPNGourmet import ascii, warn, crit, test
from globalsb4 import check

#Required dor colored to work on Windows.
os.system("")

#Get authtoken from file.
with open("../_authtoken.txt") as f:
    authtoken = f.readlines()
authtoken = [x.strip() for x in authtoken]
authtoken = authtoken[0]

# Predefined variables.
prefix = "&"
description = """SizeBot4 is a complete rewrite of SizeBot for the Size Matters server.
Written by DigiDuncan.
The SizeBot Team: DigiDuncan, AWK_, Arceus3521, SurgeTheRaichu."""
initial_extensions = ["cogs.register",
    "cogs.mod",
    "cogs.roleplay",
    "cogs.fun",
    "cogs.monika"]

# Obviously we need this printed in the terminal.
print(bg(24) + fg(202) + style.BOLD + ascii + style.RESET)

bot = commands.Bot(command_prefix=prefix, description=description)
bot.remove_command("help")
bot.add_check(check)

@bot.event
#Output header.
async def on_ready():
    print(fore.CYAN + 'Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------' + style.RESET)
    await bot.change_presence(activity=discord.Game(name="Ratchet and Clank: Size Matters"))
    print(warn("Warn test."))
    print(crit("Crit test."))
    print(test("Test test."))
    
# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
    for extension in initial_extensions:
        #try:
        bot.load_extension(extension)
    bot.run(authtoken)
