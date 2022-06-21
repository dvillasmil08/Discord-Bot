import discord
from discord.ext import commands


bot = commands.Bot(command_prefix = '.')

# bot replays with hello when calling .hello
@bot.command()
async def hello(ctx):
    await ctx.reply('Hello!')


@bot.command()
async def hello(ctx):
    await ctx.reply('Hello!')

bot.run(config.token)