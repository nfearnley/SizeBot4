import os

import discord
from discord.ext import commands

from sizebot4 import conf
from sizebot4 import logging
from sizebot4.globalsb4 import bancheck

# Required for colored to work on Windows
# TODO: Do something with this?
os.system("")

# Get authtoken from file
with open(conf.authtoken_path) as f:
    authtoken = f.readline().strip()

# Print banner to console
logging.banner(conf.banner)

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
    await bot.change_presence(activity=discord.Game(name="Ratchet and Clank: Size Matters"))
    logging.info(
        "Logged in as\n"
        f"{bot.user.name}\n"
        f"{bot.user.id}\n"
        "------")
    logging.warn("Warn test.")
    logging.crit("Crit test.")
    logging.test("Test test.")


def main():
    bot.run(authtoken)


if __name__ == "__main__":
    main()
