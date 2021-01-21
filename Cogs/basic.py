from discord.ext import commands


class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, ex):
        print(ex)
        await ctx.send("Please check with $help the usage of this command")

    @commands.command(brief="The bot developer")
    async def Leonard(self, ctx):
        await ctx.send("Warda")

    @commands.command(brief="Sends a invite in the channel")
    @commands.guild_only()
    async def invite(self, ctx):
        link = await ctx.channel.create_invite(max_age=1)
        await ctx.send(link)



def setup(bot):
    bot.add_cog(Basic(bot))

