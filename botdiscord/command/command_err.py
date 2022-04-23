import discord
import sys
import traceback
from discord.ext import commands


class CommandErrHandler(discord.ext.commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.bot.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, discord.ext.commands.CommandNotFound):
            await ctx.send('Command not found !!')
        else:
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

            ##
            
