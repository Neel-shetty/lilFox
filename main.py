import discord
import random
from discord.ext import commands, tasks
from datetime import datetime

client = commands.Bot(command_prefix = 'fox,')

#EVENTS

@client.event
async def on_ready():
    print('Woof, someone call me?')
    await client.change_presence(activity=discord.Game(name="discord with @NewFox"))

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')


#COMMANDS
#@client.command()
#async def help(ctx):
#    await ctx.send("```fox,question <insteert question here>        \\to ask yes/no questions\nfox,ping         \\for latency\nnew commands coming soon```")  

#@client.command()
#async def hello(ctx):
#    await ctx.send("Hello, i am lilfox created by NewFox#4051 \n Nice to mett you guys! :yay: ")  

@client.command()
async def ping(ctx):
    await ctx.send(f'pong! \n{client.latency*1000}ms')   
    
@client.command()
async def ques(ctx,*,question):
    responses = ['yes',
                 'maybe',  
                 'no']
    await ctx.send(f'{random.choice(responses)}')

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)       

@client.command()       #letmegooglethat.com shortcut
async def howto(ctx,*,question):
    await ctx.send 


    
   
   
   
client.run('ODAxNTUxMDgzNDcwMDYxNTY4.YAiUng.6Y7jMnuWk1NMpcPhpH50-Mt2iXY')
 






