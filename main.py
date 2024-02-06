import discord
import typing
import time

intents = discord.Intents.default ()
intents.message_content = True

client = discord.Client (intents=intents)

@client.event
async def on_ready ():
    print (f'LOGGED IN: User @{client.user}.')

@client.event
async def on_message (msg : discord.Message):
    if msg.author == client.user:
        return
    
    print (f'Logged message from: {msg.author}')
    print (f'\tMessage content: ')

    msg_content_printable = msg.content.replace ("\n", "\n\t")
    print (f'\t{ msg_content_printable }\n---\n')

@client.event
async def on_thread_create (thread : discord.Thread):
    channel : discord.TextChannel = thread.parent
    print (f"Thread created in channel: {channel.name}\n\n")

    msgs : list[discord.Message] = [message async for message in channel.history (limit=5)]

    msg : discord.Message
    for msg in msgs:
        print (msg.author.name + ": " + msg.content + "\n" + str (msg) + "\n\n")
        await msg.delete ()
        break
    
    print ('Process completed')

client.run ('MTIwNDUyMzUxMjAyMzIyMDI0OA.GPt71U.I_JU1HzLsjmtPW0kYARdxm2QsbmjfRobLtTV0c')