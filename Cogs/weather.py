import random
import discord
from discord.ext import commands
import requests
import json
from main import key


api_key = key


class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="weather")
    async def weather(self, ctx, *, location=None):
        try:
            if location is None:
                await ctx.send("Please write after weather the city name. Example: `$weather Berlin`")

            else:
                url = f" http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
                data = json.loads(requests.get(url).content)

                data = data['main']
                del data['humidity']
                del data['pressure']

                key_features = {
                    'temp': 'Temperature',
                    'feels_like': 'Feels Like',
                    'temp_min': 'Minimum Temperature',
                    'temp_max': 'Maximum Temperature'
                }

                location = location.title()
                embed = discord.Embed(
                    title=f"{location} Weather",
                    description=f"Here is the weather data for {location}.",
                    colour=random.randint(0, 0xffffff))
                for key in data:
                    embed.add_field(name=key_features[key], value=str(data[key]), inline=False)

                await ctx.send(embed=embed)


        except KeyError:
            embed = discord.Embed(title="Error", description=f'There was an error retrieving weather data for {location}.')
            await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Weather(bot))
