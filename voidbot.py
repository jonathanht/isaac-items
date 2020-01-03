#bot.py #replace input() with message
import os
import discord

from dotenv import load_dotenv
load_dotenv()


token="NjYyNDMwMjYzMTExOTc0OTIz.Xg6QZg._4V_ft5K478YsDyHk_HAuytxyUQ"

client = discord.Client()


@client.event
async def on_ready():
	print(f'{client.user} has connected to Discord!')





@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'daniel':
        response = 'is the best in the game'
        await message.channel.send(response)

    if message.content == 'kevin':
        response = 'go kevi go kevi'
        await message.channel.send(response)
    if message.content.lower().startswith('!slice'):
        user = message.content[len('!slice'):]
        response = 'https://tenor.com/view/kimetsu-no-yaiba-zenitsu-demon-slayer-lightning-breathing-iai-gif-14394969 \nthis is totally me when i''m slicing ' + str(user) + ' head off'
        await message.channel.send(response)
client.run(token)

