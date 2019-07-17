import os

import discord
from discord.ext import commands
from colored import bg, fg, fore, style

from sizebot4 import conf
from sizebot4.DPNGourmet import banner, warn, crit, test
from sizebot4.globalsb4 import bancheck

# Required for colored to work on Windows
os.system("")

# Get authtoken from file
with open(conf.authtoken_path) as f:
    authtoken = f.readline().strip()

# Print banner to console
print(f"{bg(24)}{fg(202)}{style.BOLD}\n{banner}{style.RESET}")

# Instantiate bot
description = (
    "SizeBot4 is a complete rewrite of SizeBot for the Size Matters server.\n"
    "Written by DigiDuncan.\n"
    "The SizeBot Team: DigiDuncan, AWK_, Arceus3521, SurgeTheRaichu.")
bot = commands.Bot(command_prefix=conf.prefix, description=description)

# Setup commands
bot.remove_command("help")  # TODO: Might want to consider just extending this in the future
bot.add_check(bancheck)

# Load extensions (cogs)
initial_extensions = [
    "register",
    "mod",
    "roleplay",
    "fun",
    "monika"
]
for extension in initial_extensions:
    bot.load_extension(f"sizebot4.cogs.{extension}")


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


def main():
    bot.run(authtoken)


if __name__ == "__main__":
    main()
