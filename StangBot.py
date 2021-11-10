import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '-')
TOKEN = 'OTA3NzgzMzY0NjAwMjcwODU4.YYsNIw.0-Aawrkj1aQwtJvgf_Pe-153kN0'

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

client.run(TOKEN)
