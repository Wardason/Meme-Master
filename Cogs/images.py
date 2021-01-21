from discord.ext import commands
import aiohttp
import discord

class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(brief="Sends a random cat image")
    async def cat(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("http://aws.random.cat/meow") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Meow")
                    embed.set_image(url=data['file'])
                    embed.set_footer(text="http://random.cat/")

                    await ctx.send(embed=embed)


    @commands.command(brief="Sends a random dog image")
    async def dog(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://random.dog/woof.json") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Woof")
                    embed.set_image(url=data['url'])
                    embed.set_footer(text="http://random.dog/")

                    await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Images(bot))