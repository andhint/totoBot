import asyncio
import os

import discord
from discord.ext import commands

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD")

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='blesstherains', help='¯\_(ツ)_/¯')
async def bless_the_rains(ctx):
    if ctx.author.voice is None or ctx.author.voice.channel is None:
        return

    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
        vc = await voice_channel.connect()
    else:
        await ctx.voice_client.move_to(voice_channel)
        vc = ctx.voice_client

    vc.play(discord.FFmpegPCMAudio('africa.webm'))
    await asyncio.sleep(60*4 + 34 + 5)
    await vc.disconnect()   

@bot.command(name='plsstop', help='¯\_(ツ)_/¯')
async def pls_stop(ctx):
    if ctx.voice_client is not None:
        vc = ctx.voice_client
        await vc.disconnect()

bot.run(TOKEN)