import discord
from discord.ext import commands
from datetime import datetime

class nmCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        print("ping")
        await ctx.reply("hello")

    @commands.command()
    async def sync(self, ctx):
        fmt = await ctx.bot.tree.sync(guild=ctx.guild)
        # await ctx.send(fmt)
        names = [command.name for command in fmt]

        await ctx.send(f"Synced {names}")

async def setup(bot):
    await bot.add_cog(nmCommand(bot), guilds=[discord.Object(id=785708140959760414)])