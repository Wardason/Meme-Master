from discord.ext import commands
import discord
import random

messages = [":8ball:As I see it, yes.", ":8ball: yes!!!!", ":8ball:Yes – definitely.", ":8ball: sure, why not",
            ":8ball: hell to the yes",
            ":8ball: that would be a hell no", ":8ball: lol literally no", ":8ball: No, you idiot",
            ":8ball: no lmfao", ":8ball: ask again later when I'm less busy with ur mum"
            ]


class Fun(commands.Cog):
    def __init__(self, bot):
        self.f = None
        self.bot = bot

    @commands.command(brief="Returns your gay rate in percent")
    async def gay(self, ctx):
        number = random.randint(0, 100)
        percent = "You are " + str(number) + "% gay :gay_pride_flag:"

        color = random.randint(0, 0xffffff)
        embed = discord.Embed(title="gay r8 machine", description=percent, colour=color)
        await ctx.channel.send(embed=embed)

    @commands.command(brief="Returns your simp rate in percent")
    async def simp(self, ctx):
        number = random.randint(0, 100)
        percent = "You are " + str(number) + "% simp"

        color = random.randint(0, 0xffffff)
        embed = discord.Embed(title="simp r8 machine", description=percent, colour=color)
        await ctx.channel.send(embed=embed)

    @commands.command(name="8ball")
    async def ball(self, ctx, question=None):
        if question is None:
            await ctx.send("What are you asking the 8ball?")
        else:
            answer_from_8ball = random.choice(messages)

            color = random.randint(0, 0xffffff)
            embed = discord.Embed(title=":8ball: prediction", description=answer_from_8ball, colour=color)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Fun(bot))
