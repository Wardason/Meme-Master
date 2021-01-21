from discord.ext import commands
import discord
from utils import get_momma_jokes



class MamaJokes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="")
    async def insult(self, ctx):
        insult = await get_momma_jokes()
        await ctx.send(insult)


def setup(bot):
    bot.add_cog(MamaJokes(bot))