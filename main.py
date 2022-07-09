# bot.py
# TabNi
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
import nsfw_dl
import pytest

intents = discord.Intents.default()
intents.members = True
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') #token
PREFIX = os.getenv('PREFIX')
GUILD = os.getenv('DISCORD_GUILD') #its not defined, dont remember why, but still works
client = Bot(description="Bot para grupo pronomy https://discord.gg/xqfW8jE", command_prefix=PREFIX, pm_help = False, intents=intents)
ctx ='*args' #it is a bug fix for my first try in making commands, i dont know why, but it happened
novatos = 'novos-membros'
desertores = 'cantinho-da-vergonha'
novaoi = "Bem Vindo espero que aproveite o grupo, de uma passada no #cargos-ez para ter acesso a alguns lugares que talvez voce goste"
desertchau = "Espero que tenha gostado do tempo que tenha passsado com a gente. Sentimos que tenha saido, mas caso queira volta, sempre estamos abertos para recebe-lo novamente"

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
        if str(channel) == novatos: #when someone enter, here is the channel tha will be sended the message
            global novaoi
            await channel.send(f'{member.mention} '+ novaoi) # welcome message
            await member.send(f"('っ◔◡◔)っ ♥ Ola! {member} seja bem vindo ao *PRONOMY*, EU SOU UM BOT PROGRAMADO PELO ADM PARA AJUDAR EM COISAS GERAIS DO SERVER, CASO TENHA ALGUMA DUVIDA TEMOS A SESSÃO 'REGRAS' EM UM DOS PRIMEIROS CANAIS, QUALQUER COISA SÓ CHAMAR O/ ♥") #DM to new member
            print(f"{member} entrou no server.")
            return


#SAIU

@client.event
async def on_member_remove(member):
    for channel in member.guild.channels:
        if str(channel) == desertores: #when someone leave, here is the channel tha will be sended the messsage
            await channel.send(f'{member} '+ desertchau ) #message of "goodbye" but only still members can see
            print(f"{member} saiu do server.")
            return


@client.group(hidden=True)
async def sets(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send('Comando invalido, adicione entrada ou saida para determinar quais serao os canais usados')

# definindo canal de entrada
@sets.command(brief='altera canal de novos membros', description='altera canal de novos membros')
async def entrada(ctx, arg):
    global novatos
    novatos = arg
    await asyncio.sleep(3)
    await ctx.send(f"setado para {novatos}, mesmo que não exista, tá la")

# definindo mensagem do canal de entrada
@sets.command(brief='altera mensagem de novos membros', description='altera a mensagem enviada no canal de novos membros')
async def bemvindo(ctx, *, args):
    global novaoi
    novaoi = args
    await asyncio.sleep(3)
    await ctx.send(f"mensagem setada para: {novaoi}")

# definindo canal de saida
@sets.command(brief='altera canal de membros que sairam', description='altera canal de membros que sairam :(')
async def saida(ctx, arg):
    global desertores
    desertores = arg
    await asyncio.sleep(3)
    await ctx.send(f"setado para {desertores}, mesmo que não exista, tá la")

# definindo mensagem do canal de saida
@sets.command(brief='altera mensagem de membros que sairam', description='altera a mensagem enviada no canal que mostra os desertores do grupo')
async def adeus(ctx, *, args):
    global desertchau
    desertchau = args
    await asyncio.sleep(3)
    await ctx.send(f"mensagem setada para: {desertchau}")

# test command
@client.command(hidden=True, brief='ping padrão, mas é o teste', description='novas tecnologias, mais avançadas ainda são testadas aqui :)')
async def test(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send(":ping_pong: iarruuuul!!")
    await asyncio.sleep(3)
    await ctx.send("essa é uma nova era")

#limpeza
@client.command(hidden=True)
@commands.has_role("ADM") 
async def limpeza(ctx):
    await ctx.channel.purge(limit=50)

# basic ping command
@client.command(brief='ping padrão', description='novas tecnologias são testadas aqui :)')
async def ping(ctx):
	await ctx.send(':ping_pong: Pong {0.author.mention}'.format(ctx))

#realistic penny coinflip 

@client.command(brief='Lancemos uma moeda para definir esta batalha mortal', description='podem vir 3 coisas para voce nesse jogo de pura sorte cara, coroa e de pé 1 em 6000')
async def moeda(ctx):
    x = random.randint(1, 6000)
    if x == 1:
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
    elif get % 2 != 0:
            await ctx.send('Jogando a moeda'.format(ctx))
            await ctx.send('pling'.format(ctx))
            await asyncio.sleep(2)
            await ctx.send('e o que caiu foi...'.format(ctx))
            await asyncio.sleep(1)
            await ctx.send('Caiu Coroa! parabens para quem escolheu Coroa :crown:'.format(ctx))
            return
    else:
            await ctx.send('Jogando a moeda'.format(ctx))
            await ctx.send('pling'.format(ctx))
            await asyncio.sleep(2)
            await ctx.send('e o que caiu foi...'.format(ctx))
            await asyncio.sleep(1)
            await ctx.send('Caiu Cara! parabens para quem escolheu Cara :upside_down:'.format(ctx))
            return

#future NSFW command
        
@client.command(brief='isso daqui é para pervertidos', description='pesquisa qualquer coisa nsfw em relação a 2D(seu pervertido, entrou aqui pra saber o que isso faz né?)')
@commands.is_nsfw()
async def poke(ctx, *, args):
    with nsfw_dl.NSFWDL() as dl:
        img = dl.download("DanbooruSearch", args=f'{args}')
        assert img
        await ctx.send(img)

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
    await ctx.send('24/10/2020')
    await ctx.send('Fala pessoal, beleza?')
    await ctx.send('Eu sou a Venuz, a bot do servidor, e venho aqui anunciar os updates para vocês :D')
    await ctx.send('https://www.youtube.com/watch?v=attUrDwfdr8')
    await ctx.send('o que aconteceu nessa atualização foi o seguinte:')
    await ctx.send('ACABOU A PORRA DOS ROJÃO SEUS PORRA, AEEEEEEE KARALHO'.format(ctx))
    await ctx.send('E um comando novo para a moderacao dos chats'.format(ctx))
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


#forbidden list
forb = [ "-play som de rojao",
         "-play som rojao",
         "-play som rojao alto",
         "-play som de rojao alto",
         "-play rojao alto",
         "-play som de rojao auto",
         "-play https://www.youtube.com/watch?v=-UlxxHxi4i0"]


#forbidden things in chat, it will be auto-deleted when indentified
@client.event
async def on_message(message):
    for i in forb:
        if message.content.startswith(i):
            await message.channel.purge(limit=1)
            await asyncio.sleep(1)
            await message.channel.send('-skip'.format(message))
            await asyncio.sleep(1)
            await message.channel.purge(limit=2)

            
    await client.process_commands(message)


@desligar.error
async def desligar_error(ctx, error):    
    if isinstance(error, commands.MissingRole):
        await ctx.channel.purge(limit=1)
        await ctx.channel.send('amigo, você provavelmente não tem permissões para fazer essas parada ai')
        return

client.run(TOKEN)
