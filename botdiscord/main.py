import discord
from command.CommandBot import BotOnReady
from bot.bot import MyBot
from command.command_err import CommandErrHandler


def main():
    intents= discord.Intents.default()
    intents.members= True
    token= "OTU5MzQ5MjI2MDc1MjA5NzI4.Ykallw.xpu-xFkfd9CNhYv5hlH5k71BS_g"


    bot = BotOnReady(command_prefix='/', intents=intents)
    
    bot.add_cog(MyBot(bot))
    bot.add_cog(CommandErrHandler(bot))
    bot.run(token)

if __name__ == '__main__':
    main()
