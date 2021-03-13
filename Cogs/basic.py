import time
import random
from discord.ext import commands
from discord.ext.commands import MissingPermissions
import discord



class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(error)

        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=f"Slow down 🤯",
                               description=f'That command is on cooldown. Try again in: \n ``{error.retry_after:.2f} sec``.',
                               color=random.randint(0, 0xffffff))
            await ctx.send(embed=em)

        elif isinstance(error, MissingPermissions):
            em = discord.Embed(title=f"Missing permissions",
                               description=f"I'm sorry, you haven't permissions for that 🥺.",
                               color=random.randint(0, 0xffffff))
            await ctx.send(embed=em)

        else:
            await ctx.send("Please check with $help the usage of this command")

    @commands.command(brief="The bot developer")
    async def developer(self, ctx):
        embed = discord.Embed()
        embed.add_field(name="", value="")
        await ctx.send("This bot is developed by Leonard Warda. Find me on:\nTwitter: Wardason_\nInstagram: "
                       "leonardwarda\nGithub: Wardason")

    @commands.command(brief="F for lasse")
    async def lucylover(self, ctx):
        await ctx.channel.send("https://imgur.com/ndrIfTz")

    @commands.command(name="knecht")
    async def bene(self, ctx):
        await ctx.channel.send("https://imgur.com/a/BobfAHs")
        time.sleep(1)
        await ctx.channel.send("spaß")


def setup(bot):
    bot.add_cog(Basic(bot))
