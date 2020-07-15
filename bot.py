# bot.py
# TabNi
import os

import discord
import random
import asyncio
import platform
from dotenv import load_dotenv
from discord.ext import commands
from discord import Game

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') #token
GUILD = os.getenv('DISCORD_GUILD') #its not defined, dont remember why, but still works
COIN = os.getenv('COINFLIP') #variables for a gambling game
bot = commands.Bot(command_prefix = "!")

#LOG LIGADO

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print('Logged in as')
    print(bot.user)
    print('@720274020607590490') #here i forced the @, u can change it, in future i'll change it so that u dont need to change
    print(discord.__version__)
    print('------')

    print('Servers connected to:')
    for server in bot.guilds:
        print(server.name)

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}') #useless logging log


#ENTROU

@bot.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "chegada-dos-desconhecidos": #when someone enter, here is the channel tha will be sended the message
            await channel.send(f"""Bem Vindo {member} espero que aproveite o grupo, de uma passada no #cargos-ez para ter acesso a alguns lugares que talvez voce goste""") # "welcome" message
            await member.send(f"('っ◔◡◔)っ ♥ Ola! {member} seja bem vindo ao *PRONOMY*, EU SOU UM BOT PROGRAMADO PELO ADM PARA AJUDAR EM COISAS GERAIS DO SERVER, CASO TENHA ALGUMA DUVIDA TEMOS A SESSÃO 'REGRAS' EM UM DOS PRIMEIROS CANAIS, QUALQUER COISA SÓ CHAMAR O/ ♥") #DM to new member
            print(f"{member} entrou no server.")
            return


#SAIU

@bot.event
async def on_member_remove(member):
    for channel in member.guild.channels:
        if str(channel) == "cantinho-da-vergonha": #when someone leave, here is the channel tha will be sended the messsage
            await channel.send('Ｅｓｐｅｒｏ ｑｕｅ ｔｅｎｈａ ｇｏｓｔａｄｏ ｄｏ ｔｅｍｐｏ ｑｕｅ ｐａｓｓｏｕ ｃｏｍ ａ ｇｅｎｔｅ． Ｓｅｎｔｉｍｏｓ ｑｕｅ ｔｅｎｈａ ｓａｉｄｏ， ｍａｓ ｃａｓｏ ｑｕｅｉｒａ ｖｏｌｔａｒ， ｓｅｍｐｒｅ ｅｓｔａｍｏｓ ａｂｅｒｔｏｓ ａ ｒｅｃｅｂｅｒ－ｌｏ ｎｏｖａｍｅｎｔｅ') #message of "goodbye" but only still members can see
            print(f"{member} saiu do server.")
            return

#DESLIGAR

@bot.event
async def on_message(message):
    if message.content.startswith("p!desligar"): #command to turn of the bot
        await message.channel.send('Desligando... {0.author.mention}'.format(message))
        await asyncio.sleep(3)
        await message.channel.send('Desligado'.format(message))
        await bot.logout()
    if message.content.startswith("p!ping"): #simple ping
        await message.channel.send('Pong {0.author.mention}'.format(message))
    if message.content.startswith("p!help moeda"): #first help, its the coinflip help
        await message.channel.send('podem vir 3 coisas para voce nesse jogo de pura sorte cara, coroa e de pé 1 em 6000'.format(message))
    if message.content.startswith("p!moeda"): #coinflip
        x = (COIN)
        (random.choice(x))
        if (random.choice(x)) == "U":
            await message.channel.send('Jogando a moeda'.format(message))
            await message.channel.send('pling'.format(message))
            await asyncio.sleep(2)
            await message.channel.send('e o que caiu foi...'.format(message))
            await asyncio.sleep(1)
            await message.channel.send('caiu Cara! parabens para quem escolheu Cara :upside_down:'.format(message))
            return
        elif (random.choice(x)) == "O":
            await message.channel.send('Jogando a moeda'.format(message))
            await message.channel.send('pling'.format(message))
            await asyncio.sleep(2)
            await message.channel.send('e o que caiu foi...'.format(message))
            await asyncio.sleep(1)
            await message.channel.send('Caiu Coroa! parabens para quem escolheu Coroa :crown:'.format(message))
            return
        elif (random.choice(x)) == "I":
            await message.channel.send('Jogando a moeda'.format(message))
            await message.channel.send('pling'.format(message))
            await asyncio.sleep(2)
            await message.channel.send('e o que caiu foi...'.format(message))
            await asyncio.sleep(1)
            await message.channel.send('perai, como assim?'.format(message))
            await asyncio.sleep(1)
            await message.channel.send('...'.format(message))
            await message.channel.send('Por essa nem eu esperava, isso acontece uma vez a cada 6000 jogadas, Parabens voce jogou a moeda de PÉ :arrow_up:')
            return
        
#LIGAR BOT

bot.run(TOKEN)
