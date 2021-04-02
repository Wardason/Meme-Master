from discord.ext import commands
import discord
import random
import time

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

        embed = discord.Embed(title="gay r8 machine", description=percent, colour=random.randint(0, 0xffffff))
        await ctx.channel.send(embed=embed)

    @commands.command(brief="Returns your simp rate in percent")
    async def simp(self, ctx):
        number = random.randint(0, 100)
        percent = "You are " + str(number) + "% simp"

        embed = discord.Embed(title="simp r8 machine", description=percent, colour=random.randint(0, 0xffffff))
        await ctx.channel.send(embed=embed)

    @commands.command(name="8ball")
    async def ball(self, ctx, question=None):
        if question is None:
            await ctx.send("What are you asking the 8ball?")
        else:
            answer_from_8ball = random.choice(messages)
            await ctx.send(answer_from_8ball)

    @commands.command(name="hack")
    async def hack(self, ctx, target=None):
        if target is None:
            await ctx.send("Who are we hacking?")
        else:
            await ctx.send(f"Hacking {target} now...")
            time.sleep(1)
            await ctx.send("Finding Ip Adress")
            time.sleep(2)
            await ctx.send("Ip Adress: 168.212. 226.204")
            time.sleep(1)
            await ctx.send("Selling data to the Goverment")
            time.sleep(1)
            await ctx.send("Reporting account to discord for breaking TOS...")
            time.sleep(1)
            await ctx.send(f"Finished hacking {target} \n Congrats")

    @commands.command()
    async def lenny(self, ctx):
        await ctx.send("( ͡° ͜ʖ ͡°)")

    @commands.command()
    async def say(self, ctx, *, args="Im to dumb to use this command"):
        name = ctx.message.author.name

        await ctx.send(f"{args}\n -**{name}**")






def setup(bot):
    bot.add_cog(Fun(bot))
