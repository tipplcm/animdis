import discord
import asyncio
import time
import uuid
import threading

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('1'):
        client.loop.create_task(scrollNick(message))

async def scrollNick(message):
    nick = client.user.name
    string = "_________"
    while True:
        for i in range(len(string)):
            #new_nick = nick[:i] + nick[i].swapcase() + nick[i+1:] 
            
            new_nick = "_" + string[:i] + nick + string[i+1:] + "_"
            await client.change_nickname(message.server.me, new_nick) 

token="MjQzODM0MjEwMDI3MTc1OTM3.DYCfGA.r7nZc70hi6qw-jaGUHSlxeKaST0"
client.run(token ,bot=False)
