import discord
import os
import time

intents = discord.Intents(messages=True, message_content=True, voice_states=True)
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_read():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$lookinggood'):
        await message.channel.send('my man!')

@client.event
async def on_voice_state_update(member, before, after):
    if before.channel == None and after.channel != None:
        channel = client.get_channel(850843483781464087)
        jumpurl = after.channel.jump_url
        await channel.send(member.display_name + ' has just joined the ' + after.channel.name + ' channel')
        await channel.send(jumpurl)
        print(member.display_name + ' has just joined the ' + after.channel.name)

client.run('MTA2ODMxMDUzNDM2NzIxNTY2Nw.Gby1eb.PnCqDmVzDlLTpPnzAFcawsc8k25-QYxQhEGENs')
