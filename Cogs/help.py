from discord.ext import commands
import discord
import random


class Config(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="The bot developer")
    async def help(self, ctx, category=None):

        if category is None:
            embed = discord.Embed(title="Meme Master Command List", description="", colour=random.randint(0, 0xffffff))

            embed.add_field(name=":nerd:  Facts", value="`$help facts`", inline=True)
            embed.add_field(name=":camera: Image", value="`$help image`", inline=True)
            embed.add_field(name=":joy: Memes", value="`$help meme`", inline=True)
            embed.add_field(name=":smile: Fun", value="`$help fun`", inline=True)
            embed.add_field(name=":moneybag: Economy", value="`$help economy`", inline=True)
            embed.add_field(name=":tools: Utility", value="`$help utility`", inline=True)
            embed.add_field(name=":gear:  Config", value="`$help config`", inline=True)
            embed.set_footer(text="use $ before each command!")
            await ctx.send(embed=embed)

        elif category == "facts":
            embed = discord.Embed(title=":nerd: Fact commands", colour=random.randint(0, 0xffffff))
            embed.add_field(name="Commands:", value="`fact dog`, `fact cat`, ` fact panda`, `fact fox`, "
                                                    "`fact bird`, "
                                                    "`fact koala`", inline=True)
            embed.set_footer(text="use $ before each command!")
            await ctx.send(embed=embed)

        elif category == "image":
            embed = discord.Embed(title=":camera: Image commands", colour=random.randint(0, 0xffffff))
            embed.add_field(name="Commands:", value="`foodporn`", inline=True)
            embed.add_field(name="Animals:", value="`dog`, `cat`, `panda`, `bird`, `fox`, `koala`", inline=False)
            embed.set_footer(text="use $ before each command!")
            await ctx.send(embed=embed)

        elif category == "meme":
            embed = discord.Embed(title=":joy: Memes commands", colour=random.randint(0, 0xffffff))
            embed.add_field(name="Commands:", value="`meme`, `animeme`, `facepalm`", inline=True)
            embed.set_footer(text="use $ before each command!")
            await ctx.send(embed=embed)

        elif category == "fun":
            embed = discord.Embed(title=":smile: Fun commands", colour=random.randint(0, 0xffffff))
            embed.add_field(name="Commands:", value="`8ball`,`gay`, `simp`,`hack`, `insult`. `lenny`, `say`", inline=True)
            embed.set_footer(text="use $ before each command!")
            await ctx.send(embed=embed)

        elif category == "economy":
            embed = discord.Embed(title=":moneybag: Economy commands", colour=random.randint(0, 0xffffff))
            embed.add_field(name="Commands:", value="`balance`, `withdraw`, `bank`, `slots`, `send`, `rob`, "
                                                    "`leaderboard` `beg`, `daily`, `coin`", inline=True)
            embed.set_footer(text="use $ before each command!")
            await ctx.send(embed=embed)

        elif category == "utility":
            embed = discord.Embed(title=":tools: Utility commands", colour=random.randint(0, 0xffffff))
            embed.add_field(name="Commands:", value="`weather `, `news`, `wiki`, `tag`", inline=True)
            embed.set_footer(text="use $ before each command!")
            await ctx.send(embed=embed)

        elif category == "config":
            embed = discord.Embed(title=":gear:  Config commands", colour=random.randint(0, 0xffffff))
            embed.add_field(name="Commands:", value="`serverinfo`. `userinfo`, `ping`, `vote`", inline=True)
            embed.add_field(name=":warning: Important :warning: ", value="For this command the bot needs Admin "
                                                                         "permissions", inline=False)
            embed.set_footer(text="use $ before each command!")
            await ctx.send(embed=embed)

        elif category == "nsfw":
            embed = discord.Embed(title=":smirk: NSFW Commands", colour=random.randint(0, 0xffffff))
            embed.set_footer(text="use $ before each command!")
            await ctx.send(embed=embed)




def setup(bot):
    bot.add_cog(Config(bot))
