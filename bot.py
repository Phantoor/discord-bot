import discord
import asyncio
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('го'):
        await client.send_message(message.channel, 'Кушать го :cooking:')
    elif message.content.startswith('бля'):
        await client.send_message(message.channel, 'ЧТО ТЫ СКАЗАЛ!:rage: ')
    elif message.content.startswith('когда'):
        await client.send_message(message.channel, 'через час!')
    elif message.content.startswith('Когда'):
        await client.send_message(message.channel, 'через час!')
    elif message.content.startswith('КОГДА'):
        await client.send_message(message.channel, 'через час!')
    
    elif message.content.startswith('хуй'):
        await client.send_message(message.channel, 'ЧТО ТЫ СКАЗАЛ!:rage::rage::rage::rage::rage::rage::rage::rage::rage::rage::rage::rage::rage::rage::rage::rage: ')
    elif message.content.startswith('играть'):
        await client.send_message(message.channel, 'А ты уроки сделал?!:rage::rage::rage::rage::rage::rage::rage::rage::rage::rage::rage::rage::rage::rage::rage::rage: ')
    elif message.content.startswith('мам'):
        await client.send_message(message.channel, 'Да')
    elif message.content.startswith('пизда'):
        await client.send_message(message.channel, 'ЧТО ТЫ СКАЗАЛ!:rage::rage::rage::rage::rage::rage::rage::rage::rage::rage::rage::rage:')
    elif message.content.startswith('можн'):
        await client.send_message(message.channel, 'Да')
    elif message.content.startswith('скажите правила'):
        await client.send_message(message.channel, 'Правила: 1. Не обзывать твою мамку(наказание: мамка у тебя заберет комп)')
    elif message.content.startswith('зач'):
        await client.send_message(message.channel, 'Иди уроки делай!')

    

client.run('NDI1MjEwODI3ODgxMDU0MjA4.DZJhGw.mMpggk9bnN4hQcXVu_EBgSKSDLQ')


