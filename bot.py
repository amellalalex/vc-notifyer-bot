import discord
import os
import time
from dotenv import load_dotenv

timeOfPreviousNotification = 0

intents = discord.Intents(messages=True, message_content=True, voice_states=True)
client = discord.Client(intents=discord.Intents.all())

load_dotenv()

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
    # Conditions
    notPreviouslyInChannel = before.channel == None and after.channel != None
    firstInChannel = len(after.channel.members) == 1
    coolDownElapsed = time.time() - timeOfPreviousNotification >= 300

    if notPreviouslyInChannel and firstInChannel and coolDownElapsed:
        channel = client.get_channel(850843483781464087)
        jumpurl = after.channel.jump_url
        await channel.send(member.display_name + ' has just joined the ' + after.channel.name + ' channel')
        await channel.send(jumpurl)
        print(member.display_name + ' has just joined the ' + after.channel.name)
        timeOfPreviousNotification = time.time()

client.run(os.getenv('TOKEN'))
