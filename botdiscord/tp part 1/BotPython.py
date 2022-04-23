import discord

default_intents= discord.Intents.default()
default_intents.members= True
client = discord.Client(intents=default_intents)

@client.event
async def on_ready():
    print("Le bot est prêt !")

@client.event
async def on_message(message):
    if message.content.lower() == "yo":
            await message.channel.send("plai  :) ", delete_after=3)
            await message.channel.send("Salut ;) ")

@client.event
async def on_member_join(member):
    new_member_channel:discord.TextChannel = client.get_channel(959378295089168404)
    await new_member_channel.send(content=f"Bienvenue dans l'avenue {member.display_name} !")

@client.event
async def on_message(message):
    if message.content.startswith("!del"):
        number = int(message.content.split()[1])
        messages = await message.channel.history(limit=number + 1).flatten()
        for each_message in messages:
            await each_message.delete()



client.run("OTU5MzQ5MjI2MDc1MjA5NzI4.Ykallw.oHUmvZffuCs16NmvOGtkW-dW70k")


