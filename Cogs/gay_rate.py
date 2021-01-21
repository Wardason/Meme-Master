from discord.ext import commands
import random

class Gay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Returns your gay rate in percent ")
    async def gay(self, ctx, *args):
        number = random.randint(0, 100)
        prozent = "You are to " + str(number) + "% gay🌈"
        await ctx.channel.send(prozent)

def setup(bot):
    bot.add_cog(Gay(bot))