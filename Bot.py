import discord

intents = discord.Intents.default()

intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hello there misterrrr")
    elif message.content.startswith('$bye'):
        await message.channel.send("nos vemos, my friend")

client.run("MTM3OTI2NDY2NjUwNDUyODA0Mg.Ggp5oJ.3Upcr9C4R0A2BXw0HaIibk5LeEf4rR1N2YO_Yg")