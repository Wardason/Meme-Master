from discord.ext import commands
import aiohttp
import discord


class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Sends a random meme")
    async def meme(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://some-random-api.ml/meme") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Meme Master")
                    embed.set_image(url=data['image'])
                    embed.set_footer(text="https://i.some-random-api.ml/")
                    await ctx.send(embed=embed)

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

    @commands.command(brief="Sends a random panda image")
    async def panda(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://some-random-api.ml/img/panda") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Your panda pic:")
                    embed.set_image(url=data['link'])
                    embed.set_footer(text="https://some-random-api.ml/img/panda")
                    await ctx.send(embed=embed)

    @commands.command(brief="Sends a random bird image")
    async def bird(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://some-random-api.ml/img/birb") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Your bird pic:")
                    embed.set_image(url=data['link'])
                    embed.set_footer(text="https://some-random-api.ml/img/birb")
                    await ctx.send(embed=embed)

    @commands.command(brief="Sends a random fox image")
    async def fox(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://some-random-api.ml/img/fox") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Your fox pic:")
                    embed.set_image(url=data['link'])
                    embed.set_footer(text="https://some-random-api.ml/img/fox")
                    await ctx.send(embed=embed)

    @commands.command(brief="Sends a random koala image")
    async def koala(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://some-random-api.ml/img/koala") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Your fox koala:")
                    embed.set_image(url=data['link'])
                    embed.set_footer(text="https://some-random-api.ml/img/koala")
                    await ctx.send(embed=embed)

    @commands.command(brief="Sends a random anime image")
    async def anime(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://jikan1.p.rapidapi.com/meta/requests/anime/today") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Your fox koala:")
                    embed.set_image(url=data['message'])
                    embed.set_footer(text="https://some-random-api.ml/img/koala")
                    await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Images(bot))
