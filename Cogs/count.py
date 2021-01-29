import dbl
import discord
from discord.ext import commands


class TopGG(commands.Cog):
    """Handles interactions with the top.gg API"""

    def __init__(self, bot):
        self.bot = bot
        self.token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9" \
                     ".eyJpZCI6Ijc4MjI3NDk1OTg0OTY4NDk5MyIsImJvdCI6dHJ1ZSwiaWF0IjoxNjExNzQxMTEyfQ" \
                     ".p8MeIPrkYO0tORkh49JzzVza-WvM269vTVDcEPAdHPs "
        self.dblpy = dbl.DBLClient(self.bot, self.token, autopost=True)  # Autopost will post your guild count every
        # 30 minutes

    async def on_guild_post(self):
        print("Server count posted successfully")


def setup(bot):
    bot.add_cog(TopGG(bot))
