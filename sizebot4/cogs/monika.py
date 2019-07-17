import random

from discord.ext import commands

from sizebot4.DPNGourmet import warn

monika_lines = [
    "What? I don't know anyone named Monika.",
    "I don't know anyone named Monika! hehheh...",
    "Hey wha-- er...",
    "Did someone say my n- um... Monika? Weird.",
    "I hear Monika was the best character in Doki Doki. I may be a bit biased though 'cause... never mind.",
    "Monika? :sweat_smile: Never heard of her."
]


# Easter egg
class MonikaCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:  # ignore messages from bots
            return

        detected = "monika" in message.content.lower()  # triggers when a message contains "monika", case-insensitive
        if not detected:
            return

        print(warn("Monika detected."))
        triggered = random.randrange(10) == 0  # 1 in 10 chance of triggering

        if not triggered:
            return

        print(warn("Monika triggered."))
        line = random.choice(monika_lines)
        await message.channel.send(line, delete_after=5)


# Necessary
def setup(bot):
    bot.add_cog(MonikaCog(bot))
