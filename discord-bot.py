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
    await ctx.channel.send("Inizio: " +randomwikigen.randomwikigen())
    await ctx.channel.send("Fine: " +randomwikigen.randomwikigen())
bot.run(token)
