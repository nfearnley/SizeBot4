import os

import discord
from discord.ext import commands
from colored import bg, fg, fore, style

from DPNGourmet import ascii, warn, crit, test
from globalsb4 import check

# Required for colored to work on Windows
os.system("")

# Get authtoken from file
with open("../_authtoken.txt") as f:
    authtoken = f.readline().strip()

# Predefined variables
prefix = "&"
description = (
    "SizeBot4 is a complete rewrite of SizeBot for the Size Matters server.\n"
    "Written by DigiDuncan.\n"
    "The SizeBot Team: DigiDuncan, AWK_, Arceus3521, SurgeTheRaichu.")
initial_extensions = [
    "cogs.register",
    "cogs.mod",
    "cogs.roleplay",
    "cogs.fun",
    "cogs.monika"
]

# Obviously we need this printed in the terminal
print(f"{bg(24)}{fg(202)}{style.BOLD}\n{ascii}{style.RESET}")

bot = commands.Bot(command_prefix=prefix, description=description)
bot.remove_command("help")
bot.add_check(check)


@bot.event
# Output header
async def on_ready():
    print(fore.CYAN + "Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------" + style.RESET)
    await bot.change_presence(activity=discord.Game(name="Ratchet and Clank: Size Matters"))
    print(warn("Warn test."))
    print(crit("Crit test."))
    print(test("Test test."))

# Here we load our extensions(cogs) listed above in [initial_extensions]
if __name__ == "__main__":
    for extension in initial_extensions:
        bot.load_extension(extension)
    bot.run(authtoken)
