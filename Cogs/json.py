from discord.ext import commands
from utils import get_momma_jokes, get_song



class Data(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="")
    async def insult(self, ctx):
        insult = await get_momma_jokes()
        await ctx.send(insult)

    @commands.command(brief="returns song")
    async def song(self, ctx):
        songs = await get_song()
        await ctx.send(songs)


def setup(bot):
    bot.add_cog(Data(bot))
