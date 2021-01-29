from discord.ext import commands
import praw
import random
import discord

userAgent = 'News submit bot 1.0 by /u/fuiver'
clientId = 'Oth4BZatiWYhcQ'
clientSecret = 'TlGp13Vb7-jPb2BS22cmKcyQVZtcMg'
reddit = praw.Reddit(user_agent=userAgent, client_id=clientId, client_secret=clientSecret)


class Reddit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def nudes(self, ctx):
        async with ctx.channel.typing():
            subreddit = reddit.subreddit("nudes")
            all_subs = []
            hot = subreddit.hot(limit=75)

            for submission in hot:
                all_subs.append(submission)

            random_sub = random.choice(all_subs)
            name = random_sub.title
            url = random_sub.url

            em = discord.Embed(title=name)
            em.set_image(url=url)
            await ctx.send(embed=em)

    @commands.command()
    async def boobs(self, ctx):
        async with ctx.channel.typing():
            subreddit = reddit.subreddit("boobs")
            all_subs = []
            hot = subreddit.hot(limit=50)

            for submission in hot:
                all_subs.append(submission)

            random_sub = random.choice(all_subs)
            name = random_sub.title
            url = random_sub.url

            em = discord.Embed(title=name)
            em.set_image(url=url)
            await ctx.send(embed=em)

    @commands.command()
    async def ass(self, ctx):
        async with ctx.channel.typing():
            subreddit = reddit.subreddit("ass")
            all_subs = []
            hot = subreddit.hot(limit=50)

            for submission in hot:
                all_subs.append(submission)

            random_sub = random.choice(all_subs)
            name = random_sub.title
            url = random_sub.url

            em = discord.Embed(title=name)
            em.set_image(url=url)
            await ctx.send(embed=em)

    @commands.command()
    async def mgk(self, ctx):
        async with ctx.channel.typing():
            subreddit = reddit.subreddit("MachineGunKelly")
            all_subs = []
            top = subreddit.top(limit=50)

            for submission in top:
                all_subs.append(submission)

            random_sub = random.choice(all_subs)
            name = random_sub.title
            url = random_sub.url

            em = discord.Embed(title=name)
            em.set_image(url=url)
            await ctx.send(embed=em)

    @commands.command()
    async def redditmeme(self, ctx):
        async with ctx.channel.typing():
            subreddit = reddit.subreddit("memes")
            all_subs = []
            hot = subreddit.hot(limit=50)

            for submission in hot:
                all_subs.append(submission)

            random_sub = random.choice(all_subs)
            name = random_sub.title
            url = random_sub.url

            em = discord.Embed(title=name)
            em.set_image(url=url)
            await ctx.send(embed=em)



def setup(bot):
    bot.add_cog(Reddit(bot))
