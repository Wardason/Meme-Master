from discord.ext import commands
import os



bot = commands.Bot(command_prefix="$")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f'Cogs.{filename[:-3]}')









bot.run('NzgyMjc0OTU5ODQ5Njg0OTkz.X8J0VA.ZcjhB86tSIuXxOMkGiuo7nbQhb4')