# bot.py v0.2
# TabNi          an easy way to activate TabNine, just delete i and put it again
import os

import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import random
from dotenv import load_dotenv
from discord.ext.commands import Bot
from discord.ext import commands
from discord import Game

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') #token
PREFIX = os.getenv('PREFIX')
COIN = os.getenv('COINFLIP') #variables for a gambling game
GUILD = os.getenv('DISCORD_GUILD') #its not defined, dont remember why, but still works
client = Bot(description="Bot para grupo pronomy https://discord.gg/xqfW8jE", command_prefix=PREFIX, pm_help = False)
ctx ='*args' #it is a bug fix for my first try in making commands, i dont know why, but it happened

#LOG on

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print('Logged in as')
    print(client.user)
    print(client.user.id) #there was a forced @ for the bot, but i fixed it, i guess
    print(discord.__version__)
    print('------')

    print('Servers connected to:')
    for server in client.guilds:
        print(server.name)

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}') #useless logging log

#it's all in english, even tough the bot is in portuguese, it happens cause i can speak english, and probably who can see the bot in github too, duh


#ENTROU

@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "chegada-dos-desconhecidos": #when someone enter, here is the channel tha will be sended the message
            await channel.send(f"""Bem Vindo {member} espero que aproveite o grupo, de uma passada no #cargos-ez para ter acesso a alguns lugares que talvez voce goste""") # "welcome" message
            await member.send(f"('っ◔◡◔)っ ♥ Ola! {member} seja bem vindo ao *PRONOMY*, EU SOU UM BOT PROGRAMADO PELO ADM PARA AJUDAR EM COISAS GERAIS DO SERVER, CASO TENHA ALGUMA DUVIDA TEMOS A SESSÃO 'REGRAS' EM UM DOS PRIMEIROS CANAIS, QUALQUER COISA SÓ CHAMAR O/ ♥") #DM to new member
            print(f"{member} entrou no server.")
            return


#SAIU

@client.event
async def on_member_remove(member):
    for channel in member.guild.channels:
        if str(channel) == "cantinho-da-vergonha": #when someone leave, here is the channel tha will be sended the messsage
            await channel.send('Ｅｓｐｅｒｏ ｑｕｅ ｔｅｎｈａ ｇｏｓｔａｄｏ ｄｏ ｔｅｍｐｏ ｑｕｅ ｐａｓｓｏｕ ｃｏｍ ａ ｇｅｎｔｅ． Ｓｅｎｔｉｍｏｓ ｑｕｅ ｔｅｎｈａ ｓａｉｄｏ， ｍａｓ ｃａｓｏ ｑｕｅｉｒａ ｖｏｌｔａｒ， ｓｅｍｐｒｅ ｅｓｔａｍｏｓ ａｂｅｒｔｏｓ ａ ｒｅｃｅｂｅｒ－ｌｏ ｎｏｖａｍｅｎｔｅ') #message of "goodbye" but only still members can see
            print(f"{member} saiu do server.")
            return



# test command
@client.command(hidden=True, brief='ping padrão, mas é o teste', description='novas tecnologias, mais avançadas ainda são testadas aqui :)')
async def test(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send(":ping_pong: iarruuuul!!")
    await asyncio.sleep(3)
    await ctx.send("essa é uma nova era")

# basic ping command
@client.command(brief='ping padrão', description='novas tecnologias são testadas aqui :)')
async def ping(ctx):
	await ctx.send(':ping_pong: Pong {0.author.mention}'.format(ctx))

#realistic penny coinflip 

@client.command(brief='Lancemos uma moeda para definir esta batalha mortal', description='podem vir 3 coisas para voce nesse jogo de pura sorte cara, coroa e de pé 1 em 6000')
async def moeda(ctx):
    x = (COIN)
    (random.choice(x))
    if (random.choice(x)) == "U":
            await ctx.send('Jogando a moeda'.format(ctx))
            await ctx.send('pling'.format(ctx))
            await asyncio.sleep(2)
            await ctx.send('e o que caiu foi...'.format(ctx))
            await asyncio.sleep(1)
            await ctx.send('Caiu Cara! parabens para quem escolheu Cara :upside_down:'.format(ctx))
            return
    elif (random.choice(x)) == "O":
            await ctx.send('Jogando a moeda'.format(ctx))
            await ctx.send('pling'.format(ctx))
            await asyncio.sleep(2)
            await ctx.send('e o que caiu foi...'.format(ctx))
            await asyncio.sleep(1)
            await ctx.send('Caiu Coroa! parabens para quem escolheu Coroa :crown:'.format(ctx))
            return
    elif (random.choice(x)) == "I":
            await ctx.send('Jogando a moeda'.format(ctx))
            await ctx.send('pling'.format(ctx))
            await asyncio.sleep(2)
            await ctx.send('e o que caiu foi...'.format(ctx))
            await asyncio.sleep(1)
            await ctx.send('perai, como assim?'.format(ctx))
            await asyncio.sleep(1)
            await ctx.send('...'.format(ctx))
            await ctx.send('Por essa nem eu esperava, isso acontece uma vez a cada 6000 jogadas, Parabens voce jogou a moeda de PÉ :arrow_up:')
            return

#future NSFW command
        
@client.command(brief='hey, seu pervertido', description='não tem nada para você aqui')
@commands.is_nsfw()
async def poke(ctx, arg):
    await ctx.send('se-senpai? não me chame ainda, não estou pronta >.<')

@poke.error
async def on_command_error(ctx, error):
  if isinstance(error, commands.errors.NSFWChannelRequired):
        await ctx.channel.purge(limit=1)
        await ctx.channel.send('HE-HEY, NÃO FAÇA ISSO AQUI')
        await ctx.channel.send('https://64.media.tumblr.com/9aba830fe6ade2d0ba2d53cc3f94e524/tumblr_o3chm4bVof1ta7pubo1_540.gif')
        return

#updates for LOG

@client.command(hidden=True)
async def att(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send('06/09/2020')
    await ctx.send('Fala pessoal, beleza?')
    await ctx.send('Eu sou a Venuz, a bot do servidor, e venho aqui anunciar que eu que trarei os updates para vocês :D')
    await ctx.send('https://www.youtube.com/watch?v=attUrDwfdr8')
    await ctx.send('o que aconteceu nessa atualização foi o seguinte:')
    await ctx.send('melhoras de performance comigo mesma - até pq aquele merda do {0.author.mention}é um vagabundo, tive que me arruma sozinha, acredita?'.format(ctx))
    await ctx.send('E um comando novo entrou em estagio de criacao - use p!help para mais (que aliás, eu tive que arrumar sozinha também, acreditam que esse merda do {0.author.mention} não arrumou isso também?)'.format(ctx))
    await ctx.send('||@everyone||')

#turn off command

@client.command(hidden=True)
@commands.has_role("ADM") 
async def desligar(ctx):
        await ctx.channel.purge(limit=1)
        await ctx.send('Desligando... {0.author.mention}'.format(ctx))
        await asyncio.sleep(3)
        await ctx.send('Desligado'.format(ctx))
        print('desligado')
        await client.logout()

@desligar.error
async def desligar_error(ctx, error):    
    if isinstance(error, commands.MissingRole):
        await ctx.channel.purge(limit=1)
        await ctx.channel.send('amigo, você provavelmente não tem permissões para fazer essas parada ai')
        return

client.run(TOKEN)

