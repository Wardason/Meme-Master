from discord.ext import commands
import os
import discord


bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())
bot.remove_command('help')


@bot.event
async def on_ready():
    print("Start was successful")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f'Cogs.{filename[:-3]}')

bot.run('')
