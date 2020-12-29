# bot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

##Executes a prompt to verify bot logistics----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

##Designates the character a bot uses to recieve commands-----------------------------------------------------------------------------------------------------------------------------------------------------------
client = commands.Bot(command_prefix = '-')

##Executes a prompt to verify bot logistics--------------------------------------------------------------------------------------------------------------------------------------------------------------------
@client.event
async def on_ready():

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(

        f'{client.user} has connected to Discord! \n'
        f'{guild.name}(id: {guild.id}) \n'
            
        )
        
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

##Tests if the bot is connected and operational in the requested guild----------------------------------------------------------------------------------------------------------------------------------
@client.command(aliases=['ping', 'test'])
async def _ping(ctx):
    await ctx.send(f'I am ready! \nThe current ping is {round(client.latency *1000)} ms!')

## Converts any number into a binary value------------------------------------------------------------------------------------------------------------------------------------------------------------
@client.command(name='getbin')
async def getbin(ctx, *, num):

    if num[:2] == '0b':
        try:
            num = int(num[2:], 2)
            numConverted = 'That number is already in binary!'
        except ValueError:
            numConverted = "That is not the correct base!"

    elif num[:2] == '0o':
        try: 
            num = int(num[2:], 8)
            numConverted = bin(int(num))
        except ValueError:
            numConverted = "That is not the correct base!"
        
    elif num[:2] == '0d':
        try:
            numConverted = bin(int(num[2:]))
        except ValueError:
            numConverted = "That is not the correct base!"

    elif num[:2] == '0x':
        try:
            num = int(num[2:], 16)
            numConverted = bin(int(num))
        except ValueError:
            numConverted ="That is not the correct base!"
    else:
        numConverted = "An unkown error has occured!\nTry attaching the base at the start of your number:\n 0b = binary\n 0o = octal\n 0d = decimal\n 0x = hexadecimal"
    await ctx.send(numConverted)

## Converts any number into an Octal value------------------------------------------------------------------------------------------------------------------------------------------------------------
@client.command(name='getoct')
async def getoct(ctx, *, num):

    if num[:2] == '0b':
        try:
            num = int(num[2:], 2)
            numConverted = oct(int(num))
        except ValueError:
            numConverted = "That is not the correct base!"

    elif num[:2] == '0o':
        try: 
            num = int(num[2:], 8)
            numConverted = "That number is already octal!"
        except ValueError:
            numConverted = "That is not the correct base!"
        
    elif num[:2] == '0d':
        try:
            numConverted = oct(int(num[2:]))
        except ValueError:
            numConverted = "That is not the correct base!"

    elif num[:2] == '0x':
        try:
            num = int(num[2:], 16)
            numConverted = oct(int(num))
        except ValueError:
            numConverted ="That is not the correct base!"
    else:
        numConverted = "An unkown error has occured!\nTry attaching the base at the start of your number:\n 0b = binary\n 0o = octal\n 0d = decimal\n 0x = hexadecimal"
    await ctx.send(numConverted)


## Converts any number into an decimal value------------------------------------------------------------------------------------------------------------------------------------------------------------
@client.command(name='getdec')
async def getdec(ctx, *, num):

    if num[:2] == '0b':
        try:
            num = int(num[2:], 2)
            numConverted = binaryToDecimal(num)
        except ValueError:
            numConverted = "That is not the correct base!"
    
    elif num[:2] == '0o':
        try:
            num = int(num[2:], 8)
            numConverted = octalToDecimal(num)
        except ValueError:
            numConverted = "That is not the correct base!"
    
    elif num[:2] == '0d':
        try:
            num = int(num[2:])
            numConverted = "This number is already in decimal!"
        except ValueError:
            numConverted = "That is not the correct base!"
    
    elif num[:2] == '0x':
        try:
            num = int(num[2:], 16)
            numConverted = hexadecimalToDecimal(num)
        except ValueError:
            numConverted = "That is not the correct base!"
    
    else:
        numConverted = "An unkown error has occured!\nTry attaching the base at the start of your number:\n 0b = binary\n 0o = octal\n 0d = decimal\n 0x = hexadecimal"
    await ctx.send(numConverted)


## Converts any number into an hexadecimal value------------------------------------------------------------------------------------------------------------------------------------------------------------
@client.command(name='gethex')
async def gethex(ctx, *, num):

    if num[:2] == '0b':
        try:
            num = int(num[2:], 2)
            numConverted = hex(int(num))
        except ValueError:
            numConverted = "That is not the correct base!"

    elif num[:2] == '0o':
        try: 
            num = int(num[2:], 8)
            numConverted = hex(int(num))
        except ValueError:
            numConverted = "That is not the correct base!"
        
    elif num[:2] == '0d':
        try:
            numConverted = hex(int(num[2:]))
        except ValueError:
            numConverted = "That is not the correct base!"

    elif num[:2] == '0x':
        try:
            num = int(num[2:], 16)
            numConverted = "That number is already in hexadecimal"
        except ValueError:
            numConverted ="That is not the correct base!"
    else:
        numConverted = "An unkown error has occured!\nTry attaching the base at the start of your number:\n 0b = binary\n 0o = octal\n 0d = decimal\n 0x = hexadecimal"
    await ctx.send(numConverted)

## Functions for converting to decimal when recieving a bin, oct or hex values------------------------------------------------------------------------------------------------------------------------------------------------------------

def binaryToDecimal(binary): 
      
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return decimal  

def octalToDecimal(octal): 
      
    binary1 = octal 
    decimal, i, n = 0, 0, 0
    while(octal != 0): 
        dec = octal % 10
        decimal = decimal + dec * pow(8, i) 
        octal = octal//10
        i += 1
    return decimal  

def hexadecimalToDecimal(hexadecimal): 
      
    binary1 = hexadecimal
    decimal, i, n = 0, 0, 0
    while(hexadecimal != 0): 
        dec = hexadecimal % 10
        decimal = decimal + dec * pow(16, i) 
        hexadecimal = hexadecimal//10
        i += 1
    return decimal 

#Running the client-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
client.run(TOKEN)