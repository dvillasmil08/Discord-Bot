from genericpath import commonprefix
import discord
from discord.ext import commands
import os

client = commands.bot(commonprefix='$')

@client.event
async def on_ready():
    print('!!! Bot Is Online!!!\n')

client.run(os.getenv('TOKEN'))