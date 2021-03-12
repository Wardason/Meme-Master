import discord
from discord.ext import commands
import random
import json


class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def balance(self, ctx):
        await self.open_account(ctx.author)
        user = ctx.author
        users = await self.get_bank_data()
        wallet_amt = users[str(user.id)]["wallet"]
        bank_amt = users[str(user.id)]["bank"]

        em = discord.Embed(title=f"{ctx.author.name}'s balance", colour=random.randint(0, 0xffffff))
        em.add_field(name="Wallet balance", value=wallet_amt)
        em.add_field(name="Bank balance", value=bank_amt)
        await ctx.send(embed=em)

    @commands.command()
    async def beg(self, ctx):
        await self.open_account(ctx.author)
        user = ctx.author
        users = await self.get_bank_data()

        earnings = random.randint(-100, 100)
        if earnings >= 0:
            await ctx.send(f"Someone gave you {earnings} coins!!")
        else:
            await ctx.send(f"You lost {earnings} coins!!!")


        users[str(user.id)]["wallet"] += earnings

        f = open("D:\\MeineDaten\\Programmieren\\Python\\Projekte\\Discord_Bot\\Main_Bot\\data\\bank.json", "w")
        json.dump(users, f)

    @commands.command()
    async def withdraw(self, ctx, amount=None):
        await self.open_account(ctx.author)

        if amount is None:
            await ctx.send("Please enter the amount")
            return

        bal = await self.update_bank(ctx.author)

        amount = int(amount)
        if amount > bal[1]:
            await ctx.send("You don't have that much money")
            return

        if amount < 0:
            await ctx.send("Amount must be positive")
            return

        await self.update_bank(ctx.author, amount)
        await self.update_bank(ctx.author, -1 * amount, "bank")
        await ctx.send(f"You withdrew {amount} coins!")

    @commands.command()
    async def deposite(self, ctx, amount=None):
        await self.open_account(ctx.author)

        if amount is None:
            await ctx.send("Please enter the amount")
            return

        bal = await self.update_bank(ctx.author)

        amount = int(amount)
        if amount > bal[0]:
            await ctx.send("You don't have that much money")
            return

        if amount < 0:
            await ctx.send("Amount must be positive")
            return

        await self.update_bank(ctx.author, -1 * amount)
        await self.update_bank(ctx.author, amount, "bank")
        await ctx.send(f"You deposited {amount} coins!")


    @commands.command()
    async def send(self, ctx, member: discord.Member, amount=None):
        await self.open_account(ctx.author)
        await self.open_account(member)

        if amount is None:
            await ctx.send("Please enter the amount")
            return

        bal = await self.update_bank(ctx.author)

        amount = int(amount)
        if amount > bal[1]:
            await ctx.send("You don't have that much money")
            return

        if amount < 0:
            await ctx.send("Amount must be positive")
            return

        await self.update_bank(ctx.author, -1 * amount, "bank")
        await self.update_bank(member, amount, "bank")
        await ctx.send(f"You gave {amount} coins to {member}!")

    @commands.command()
    async def slots(self, ctx, amount=None):
        await self.open_account(ctx.author)

        if amount is None:
            await ctx.send("Please enter the amount")
            return

        bal = await self.update_bank(ctx.author)

        amount = int(amount)
        if amount > bal[0]:
            await ctx.send("You don't have that much money")
            return

        if amount < 0:
            await ctx.send("Amount must be positive")
            return

        final = []
        for i in range(3):
            a = random.choice(["🍊", "🍉", "🍍"])

            final.append(a)

        await ctx.send(str(final))

        if final[0] == final[1] == final[2]:
            await self.update_bank(ctx.author, 5 * amount)
            await ctx.send(f"You won {5 * amount} Coins!!")
        else:
            await self.update_bank(ctx.author, -1 * amount)
            await ctx.send(f"You lost {-1 *amount} Coins!!")

    @commands.command()
    async def coin(self, ctx, amount=None, predict=None):
        await self.open_account(ctx.author)

        if predict is None:
            await ctx.send("Please enter your prediction (tails, head)")
            return

        if amount is None:
            await ctx.send("Please enter the amount")
            return

        bal = await self.update_bank(ctx.author)

        amount = int(amount)
        if amount > bal[0]:
            await ctx.send("You don't have that much money")
            return

        if amount < 0:
            await ctx.send("Amount must be positive")
            return

        if predict == "head":
            predict = 1
        elif predict == "tails":
            predict = 2

        flip = random.randint(1, 2)
        if flip == predict:
            await self.update_bank(ctx.author, 2 * amount)
            await ctx.send(f"You won {2 * amount} Coins!!")
        else:
            await self.update_bank(ctx.author, -1 * amount)
            await ctx.send(f"You lost {-2 * amount} Coins!!")



    @commands.command()
    async def rob(self, ctx, member: discord.Member):
        await self.open_account(ctx.author)
        await self.open_account(member)

        bal = await self.update_bank(member)

        if bal[0] < 100:
            await ctx.send("It's not worth it!")
            return

        earnings = random.randrange(0, bal[0])


        await self.update_bank(ctx.author, earnings)
        await self.update_bank(member, -1*earnings)
        await ctx.send(f"You roobed and got {earnings} coins from {member}!")



    async def open_account(self, user):
        users = await self.get_bank_data()

        if str(user.id) in users:
            return False
        else:
            users[str(user.id)] = {}
            users[str(user.id)]["wallet"] = 500
            users[str(user.id)]["bank"] = 500

        f = open("D:\\MeineDaten\\Programmieren\\Python\\Projekte\\Discord_Bot\\Main_Bot\\data\\bank.json", "w")
        json.dump(users, f)
        return True





    async def get_bank_data(self):
        f = open("D:\\MeineDaten\\Programmieren\\Python\\Projekte\\Discord_Bot\\Main_Bot\\data\\bank.json", "r")
        users = json.load(f)
        return users


    async def update_bank(self, user, change=0, mode="wallet"):
        users = await self.get_bank_data()

        users[str(user.id)][mode] += change

        f = open("D:\\MeineDaten\\Programmieren\\Python\\Projekte\\Discord_Bot\\Main_Bot\\data\\bank.json", "w")
        json.dump(users, f)

        bal = users[str(user.id)]["wallet"], users[str(user.id)]["bank"]

        return bal






def setup(bot):
    bot.add_cog(Economy(bot))
