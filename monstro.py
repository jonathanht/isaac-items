#bot.py 
import os, discord, bs4
import requests

from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

client = commands.Bot(command_prefix = '!')



@client.command(pass_context = True)
async def bday(ctx, char):
    entryName = char


    res = requests.get('https://stardewvalleywiki.com/' +  entryName.lower())
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    elems = soup.select('#infoboxdetail')

    await ctx.send(entryName.lower() + "'s birthday is on: " + elems[0].text.strip())


@client.command(pass_context = True)
async def ping(ctx, message):
    await ctx.send(message)


@client.command(pass_context = True)
async def slice(ctx, person):
    await ctx.send("https://tenor.com/view/kimetsu-no-yaiba-zenitsu-demon-slayer-lightning-breathing-iai-gif-14394969 \nthis is totally me when i'm slicing " + person + "'s head off")




@client.event
async def on_ready():
	print(f'{client.user} has connected to Discord!')

	
	
client.run(BOT TOKEN HERE) 
