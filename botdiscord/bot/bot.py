import discord
###

class MyBot(discord.ext.commands.Cog, name='MyBot module'):
    def __init__(self, bot):
        self.bot = bot

    # Réponse à hey par hey
    @discord.ext.commands.command(name="hey")
    async def command_hey(self, ctx):
        await ctx.send(f'Hey {ctx.author.name}')

    # Commande Help
    @discord.ext.commands.command(name="aide")
    async def command_help(self, ctx):
        await ctx.send('Liste de commandes : \n/hey \n/aide \n/delete <nbr_de_msg> \n/here \n/tell (Affichage nbr de commande effectée)')

    # Suppression messages + affichage nbr de messages supprimés#
    @discord.ext.commands.command(name="delete")
    async def command_del(self,ctx,number_of_message:int):
            messages = await ctx.channel.history(limit=number_of_message+1).flatten()
            cpt=0
            for each_message in messages:
                await each_message.delete()
                cpt+=1
            await ctx.channel.send(cpt + f"messages deleted by {ctx.author.name}")

    # Fct permettant au bot d'afficher le nbr de commandes effectuées par l'utilisateur
    @discord.ext.commands.command(name="tell")
    async def on_message(self, ctx):
        cpt = 0
        messages = await ctx.channel.history(limit=None).flatten()
        for i in messages:
            if i.content.startswith("/"):
                cpt+=1
        await ctx.channel.send(" %s commandes effectuées" % cpt)

    # fct de test
    @discord.ext.commands.command(name="here")
    async def addhoc_pla(self, ctx):
        await ctx.send(f'{ctx.author.name} is the GameMaster of this World')
        
    # message de bienvenue
    @discord.ext.commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'{member.mention} join the TestWorld!')



'''
    async def on_ready(self):
        self.log(f"{self.user} has connected to Discord!")

    async def on_message (self, message):
        if message.author==self.user:
            return
        self.log.infolog(f"(message.author) said: {message.content}")
        m= Message(message)
        rep=m.parsing()
        if rep:
            await message.channel.send(rep)

    

class Message:
    def __init__(self, message):
        self.message = message.content

    def parsing(self):
        if self.message.startswith("/hello"):
            return "Hello !!"
        if self.message.startswith("/help"):
            print(self.messgae)
            return "Toutes les commandes : \n /hello \n /help"
'''