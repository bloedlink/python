import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    id = client.get_guild(698444038466175037)
    if message.content == ('.hello'):
        await message.channel.send('Hi')
    elif message.content == '.online':
        await message.channel.send(f'i currently see {id.member_count -1}  scrub(s) online, scrub.')
    elif message.content == (f'is {user} online')

@client.event
async def on_ready():
    print('Bot is ready')



client.run(Discord Token)


