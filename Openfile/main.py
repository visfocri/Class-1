import discord
from discord.ext import commands
import os, random
import requests


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')
    
@bot.command()
async def mem(ctx):
    image_name = random.choice(os.listdir('./Openfile/images/'))
    with open(f'./Openfile/images/{image_name}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
    
    
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
    
def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('dog')
async def dog(ctx):
    
    image_url = get_dog_image_url()
    await ctx.send(image_url)
    
def get_fox_image_url():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('fox')
async def fox(ctx):
    
    image_url = get_fox_image_url()
    await ctx.send(image_url)
    
bot.run("MTM3OTI2NDY2NjUwNDUyODA0Mg.GzmIDR.BIXv2Sxfeyo2ehUFcntU8B6TIKE4KRvThuL9hI")