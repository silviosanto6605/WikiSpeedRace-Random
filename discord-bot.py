import os
import randomwikigen
import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '-wikirun':
        x =0
        numbers_of_links = 2
        while x<numbers_of_links:
            await message.channel.send(randomwikigen.randomwikigen())
            x=x+1


client.run(token)