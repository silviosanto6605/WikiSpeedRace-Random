import os
import randomwikigen
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="--",intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot is ready!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands)")
        
    except Exception as e:
        print(e)
        
@bot.tree.command(name="start",description="Starts the bot, which returns two random links from wikipedia.it")
async def start(interaction: discord.Interaction):
    await interaction.response.send_message(f"Inizio: {randomwikigen.randomwikigen()},\nFine:{randomwikigen.randomwikigen()}")

bot.run(token)