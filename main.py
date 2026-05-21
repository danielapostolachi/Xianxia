import logging
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), 'Xianxia', '.env'))

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='Xianxia/discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='xih_', intents=intents)


@bot.event
async def on_ready():
    try:
        await bot.load_extension("Xianxia.Bot.commands")
        print("✅ Commands loaded!")
    except Exception as e:
        print(f"❌ Failed to load commands: {e}")

    try:
        await bot.tree.sync()
        print("✅ Commands synced!")
    except Exception as e:
        print(f"❌ Failed to sync: {e}")

    print(f"We are ready to go in, {bot.user.name}")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)