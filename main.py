from discord.ext import commands
import discord
import json
import os

if os.path.exists(os.getcwd() + "/config.json"):
    with open("./config.json") as f:
        configData = json.load(f)
else:
    configTemplate = {"Token": "", "Prefix": "$"}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f)

token = configData["Token"]
prefix = configData["Prefix"]



bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())
bot.remove_command('help')


@bot.event
async def on_ready():
    print("Start was successful")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f'Cogs.{filename[:-3]}')

bot.run(token)
