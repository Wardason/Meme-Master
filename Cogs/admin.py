from typing import Optional
from discord import Member, Embed
from discord.ext import commands
import random



class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="")
    async def userinfo(self, ctx, target: Optional[Member]):
        target = target or ctx.author

        embed = Embed(title="User Information",
                      color=target.color)
        embed.set_thumbnail(url=target.avatar_url)

        fields = [("Name", str(target), False),
                  ("ID", target.id, True),
                  ("Bot?", target.bot, True),
                  ("Status", str(target.status).title(), True),
                  ("Activity", f"{str(target.activity.type).split('.')[-1].title() if target.activity else 'N/A'} "
                               f"{target.activity.name if target.activity else ''}", True),
                  ("Top role", target.top_role.mention, True),
                  ("Created at", target.created_at.strftime("%d/%m/%Y %H:%M:%S"), True),
                  ("Joined at", target.joined_at.strftime("%d/%m/%Y %H:%M:%S"), True),
                  ("Server Booster?", bool(target.premium_since), True)]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
        await ctx.send(embed=embed)

    @commands.command(brief="")
    async def serverinfo(self, ctx):
        embed = Embed(title="Server information", colour=random.randint(0, 0xffffff))

        embed.set_thumbnail(url=ctx.guild.icon_url)

        statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]

        fields = [("ID", ctx.guild.id, True),
                  ("Owner", ctx.guild.owner, True),
                  ("Region", ctx.guild.region, True),
                  ("Created at", ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S"), True),
                  ("Members", len(ctx.guild.members), True),
                  ("Humans", len(list(filter(lambda m: not m.bot, ctx.guild.members))), True),
                  ("Bots", len(list(filter(lambda m: m.bot, ctx.guild.members))), True),
                  ("Banned members", len(await ctx.guild.bans()), True),
                  ("Statuses", f"🟢 {statuses[0]} 🟠 {statuses[1]} 🔴 {statuses[2]} ⚪ {statuses[3]}", True),
                  ("Text channels", len(ctx.guild.text_channels), True),
                  ("Voice channels", len(ctx.guild.voice_channels), True),
                  ("Categories", len(ctx.guild.categories), True),
                  ("Roles", len(ctx.guild.roles), True),
                  ("Invites", len(await ctx.guild.invites()), True),
                  ("\u200b", "\u200b", True)]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        await ctx.send(embed=embed)

    @commands.command()
    async def vote(self, ctx):
        msg = 'You can support me here --> https://top.gg/bot/782274959849684993/vote'
        await ctx.send(msg)

    @commands.command()
    async def ping(self, ctx):
        ping = self.bot.latency
        ping = "%.2f" % ping
        await ctx.send(f'My ping is {ping}!')




def setup(bot):
    bot.add_cog(Admin(bot))
