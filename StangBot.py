import discord
from discord.ext import commands
from discord.ext import tasks

client = commands.Bot(command_prefix = '-')
TOKEN = 'OTA3NzgzMzY0NjAwMjcwODU4.YYsNIw.0-Aawrkj1aQwtJvgf_Pe-153kN0'

@client.event
async def on_ready():
    print('Bot is ready.')
    await client.change_presence(activity=discord.Game(name="Nothing"))
#    timed_message.start()


@client.command(hidden=True)
async def dev(ctx):
    if ctx.message.author.id == 272441750771990530:
        await ctx.send("Access Granted.")
    else:
        await ctx.send("Access Denied.")

@client.command()
async def rr(ctx):
    await ctx.author.send("Never gonna give you up!")

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason = None):
    await member.kick(reason=reason)

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason = None):
    await member.ban(reason=reason)

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Need to specify a member to kick.')

@kick.error
async def kick_error2(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('Invalid member entered.')

'''
@tasks.loop(minutes=1.0)
async def timed_message():
    channel = client.get_channel(559354490457817091)
    await channel.send("TESTING EVERY MINUTE")
'''
client.run(TOKEN)
