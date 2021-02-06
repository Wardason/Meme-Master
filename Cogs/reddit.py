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
    async def meme(self, ctx):
        async with ctx.channel.typing():
            subreddit = reddit.subreddit("memes")
            all_subs = []
            hot = subreddit.hot(limit=50)

            for submission in hot:
                all_subs.append(submission)

            random_sub = random.choice(all_subs)
            name = random_sub.title
            url = random_sub.url
            votes = random_sub.score
            comments = random_sub.num_comments

            em = discord.Embed(title=name, colour=random.randint(0, 0xffffff))
            em.set_image(url=url)
            em.set_footer(text=f"👍{votes}|💬{comments}")
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

            em = discord.Embed(title=name, colour=random.randint(0, 0xffffff))
            em.set_image(url=url)
            await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(Reddit(bot))
