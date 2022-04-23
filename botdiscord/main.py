import discord
from command.CommandBot import BotOnReady
from bot.bot import MyBot
from command.command_err import CommandErrHandler
import json




def main():
    intents= discord.Intents.default()
    intents.members= True

    ##         Mettre le token de son bot ici           ##
    token= "<votre token>"
    ######################################################

    bot = BotOnReady(command_prefix='/', intents=intents)
    
    bot.add_cog(MyBot(bot))
    bot.add_cog(CommandErrHandler(bot))
    bot.run(token)

if __name__ == '__main__':
    main()
