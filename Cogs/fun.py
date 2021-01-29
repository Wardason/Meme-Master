from discord.ext import commands
import random


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Returns your gay rate in percent")
    async def gay(self, ctx):
        number = random.randint(0, 100)
        percent = "You are " + str(number) + "% gay🌈"
        await ctx.channel.send(percent)

def setup(bot):
    bot.add_cog(Fun(bot))
