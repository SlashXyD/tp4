import discord
from discord.ext import commands

class BotOnReady(commands.Bot):
    async def on_ready(self):
        print(f'{self.user} is ready !')