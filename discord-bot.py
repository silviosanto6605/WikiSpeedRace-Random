import os
import randomwikigen
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='--')


client = discord.Client()

@bot.command(name='wikirun', help='Generate 2 random Wikipedia links')
async def random_links (ctx):
    x =0
    numbers_of_links = 2
    while x<numbers_of_links:
        await ctx.channel.send(randomwikigen.randomwikigen())
        x=x+1

       
bot.run(token)
