import datetime
from logging import Logger
import discord
from discord.ext import commands
from bot import bot

class BotOnReady(commands.Bot):
    
    date =datetime.datetime.now()
    date = date.strftime("%m/%d/%y, :%H:%M:%S")
    date = str(date)

    async def on_ready(self):
        print(f'{self.user} is ready !')

        with open("logs.txt", "a") as L :
            L.write(self.date +" bot connection\n")