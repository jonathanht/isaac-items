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
async def tenman(ctx, *args):
    #Create list of players according to args
    players = [item for item in args]
    
    #Create lists with placeholder values "None"
    team1 = [None] * 5
    team2 = [None] * 5

    #Chooses random players from player list to add into Team 1 list	
    pos = 0
    while pos < 5:
        rand = random.randint(0,9)
    	
	#Only add elements from index players that are not marked as already "chosen"
        if(players[rand] == "chosen") :
            while(players[rand] == "chosen"):
                rand = random.randint(0,9)
            team1[pos] = players[rand]


        team1[pos] = players[rand]
	
	#If the player in the list has been chosen already, replace with string "chosen"
        players[rand] = "chosen"
        pos = pos + 1


    #Adds remaining players into Team 2 
    for i in range(10):
        if(players[i] != "chosen"):
            position = 0
            team2.insert(position, players[i])
            position = position + 1
    #Remove placeholder values in indexes
    for i in range(5):
        del team2[5]
	
    #Convert lists to respective strings
    finalTeam1 = ', '.join(team1)
    finalTeam2 = ', '.join(team2)
    
    #Print both teams with discord formatting
    await ctx.send("``` Team 1: " + finalTeam1 + "```")
    await ctx.send("``` Team 2: " + finalTeam2 + "```")
    




@client.command(pass_context = True)
async def slice(ctx, person):
    await ctx.send("https://tenor.com/view/kimetsu-no-yaiba-zenitsu-demon-slayer-lightning-breathing-iai-gif-14394969 \nthis is totally me when i'm slicing " + person + "'s head off")

@client.command(pass_context = True)
async def item(ctx, char):
    entryName = char
    
    res = requests.get('https://bindingofisaacrebirth.gamepedia.com/' +  entryName)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    elems = soup.select('#mw-content-text > div > ul:nth-child(5) > li:nth-child(1)')

    await ctx.send('***' + entryName + '***\n' + '```' + elems[0].text.strip() + '```')


@client.event
async def on_ready():
	print(f'{client.user} has connected to Discord!')


client.run('insert key') 
