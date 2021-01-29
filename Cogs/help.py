from discord.ext import commands
import discord


class Config(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="The bot developer")
    async def help(self, ctx, category=None):

        if category is None:
            embed = discord.Embed(title="Meme Master Command List", description="")

            embed.add_field(name=":nerd:  Facts", value="`$help facts`", inline=True)
            embed.add_field(name=":camera: Image", value="`$help image`", inline=True)
            embed.add_field(name=":robot: Reddit", value="`$help reddit`", inline=True)
            embed.add_field(name=":joy: Memes", value="`$help meme`", inline=True)
            embed.add_field(name=":smile: Fun", value="`$help fun`", inline=True)
            embed.add_field(name=":game_die: Gamble", value="`$help gamble`", inline=True)
            embed.add_field(name=":gear:  Config", value="`$help config`", inline=True)
            embed.set_footer(text="use $ before each command!")
            await ctx.send(embed=embed)

        elif category == "facts":
            embed = discord.Embed(title=":nerd: Fact commands")
            embed.add_field(name="Commands:", value="`fact dog`, `fact cat`, ` fact panda`, `fact fox`, `fact bird`, "
                                                    "`fact koala`", inline=True)
            embed.set_footer(text="use $ before each command!")
            await ctx.send(embed=embed)

        elif category == "image":
            embed = discord.Embed(title=":camera: Image commands")
            embed.add_field(name="Commands:", value="`dog`, `cat`, `panda`, `bird`, `fox`, `koala`", inline=True)
            embed.set_footer(text="use $ before each command!")
            await ctx.send(embed=embed)

        elif category == "reddit":
            embed = discord.Embed(title=":robot: Reddit commands")
            embed.add_field(name="Commands:", value="`mgk`, `redditmeme`", inline=True)
            embed.set_footer(text="use $ before each command!")
            await ctx.send(embed=embed)

        elif category == "meme":
            embed = discord.Embed(title=":joy: Memes commands")
            embed.add_field(name="Commands:", value="`meme`, `redditmeme`", inline=True)
            embed.set_footer(text="use $ before each command!")
            await ctx.send(embed=embed)

        elif category == "fun":
            embed = discord.Embed(title=":smile: Fun commands")
            embed.add_field(name="Commands:", value="`gay`,`8ball`, `insult`", inline=True)
            embed.set_footer(text="use $ before each command!")
            await ctx.send(embed=embed)

        elif category == "gamble":
            embed = discord.Embed(title=":game_die: Gamble commands")
            embed.add_field(name="Commands:", value="`random`, `dice`, `coin`", inline=True)
            embed.set_footer(text="use $ before each command!")
            await ctx.send(embed=embed)

        elif category == "config":
            embed = discord.Embed(title=":gear:  Config commands")
            embed.add_field(name="Commands:", value="`serverinfo`. `userinfo`, `vote`", inline=True)
            embed.add_field(name=":warning: Important :warning: ", value="For this command the bot needs Admin "
                                                                         "permissions", inline=False)
            embed.set_footer(text="use $ before each command!")
            await ctx.send(embed=embed)

        elif category == "nsfw":
            embed = discord.Embed(title=":smirk: NSFW Commands")
            embed.set_footer(text="use $ before each command!")
            await ctx.send(embed=embed)




def setup(bot):
    bot.add_cog(Config(bot))
