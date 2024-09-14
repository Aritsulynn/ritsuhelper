import os
import random
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

    @commands.command()
    async def desync(self, ctx):
        self.bot.tree.clear_commands(guild=ctx.guild)
        await self.bot.tree.sync()
        await ctx.send("Desynced")


async def setup(bot):
    await bot.add_cog(
        nmCommand(bot),
        guilds=[discord.Object(id=int(i)) for i in os.getenv("guilds").split(",")],
    )
