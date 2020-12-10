import discord
from discord.ext import commands

client = commands.Bot(command_prefix='w.')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def ping(ctx):
    await ctx.send(f'{client.latency * 1000} ms')

client.run("asiuyrxAac7I_L-bWb3cBIGoiA1yKYLLHUmN67iF6YVORp10LNB12dR10Bjm-mmi4h3g")