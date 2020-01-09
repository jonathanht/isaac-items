#bot.py #replace input() with message
import os, discord, bs4, requests


from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

client = commands.Bot(command_prefix = '!')



@client.command(pass_context = True)
async def bday(ctx, char):
    res = requests.get('https://stardewvalley.wiki.com/' + char.lower())
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#infoboxdetail')
    birthday = elems[0].text.strip()
    

    await ctx.send(char.lower() + " 's birthday is on: " + birthday)





@client.command(pass_context = True)
async def slice(ctx, person):
    await ctx.send("https://tenor.com/view/kimetsu-no-yaiba-zenitsu-demon-slayer-lightning-breathing-iai-gif-14394969 \nthis is totally me when i'm slicing " + person + "'s head off")


@client.event
async def on_ready():
	print(f'{client.user} has connected to Discord!')






client.run("INSERT BOT TOKEN HERE")
