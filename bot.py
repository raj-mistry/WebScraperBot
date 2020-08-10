import discord
import random
from discord.ext import commands
from PIL import Image
from io import BytesIO
import requests
from bs4 import BeautifulSoup
import urllib.request
import PIL.Image
from graphics import *

client = commands.Bot(command_prefix='.')


bannedwords = [
    "insert",
    "your",
    "banned",
    "words",
    "here"
]


@client.event
async def on_ready():
    print('Bot is ready.')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('dice'):  # Dice Command
        num = random.randint(1, 6)
        randomint = str(num)
        await message.channel.send(randomint)

    if message.content.startswith('joke'):
        jokes = [
            "I'm fine with alchohol, cigarettes and marijuana, but coccaine is where I draw the line",
            "My grandad asked me how to print on his computer...I told him it’s Ctrl-P. He says he hasn’t been able to do that for ages.",
            "Today a man knocked on my door and asked for a small donation towards the local swimming pool. I gave him a glass of water.",
            "What do you call a blind deer? No Idea."
        ]
        num = random.randint(0, len(jokes))
        randomjoke = jokes[num]
        await message.channel.send(randomjoke)

    if message.content.startswith('!define'):
        define1 = message.content.split(' ')
        define = define1[1]

        website = 'https://www.dictionary.com/browse/'+define+'?s=t'
        source = requests.get(website).text
        soup = BeautifulSoup(source, 'html.parser')
        definition = str(soup.find_all('meta')[1])
        definition = definition.split('\"')[1]
        definition = definition.split(".")[0]

        await message.channel.send(definition)

    if message.content.startswith('!search'):
        search1 = message.content.split(' ')
        search = search1[1]
        with open('pic1.jpg', 'wb') as handle:

            searchterm = search
            # this section of the code will take a website, and
            # grab the 10th image
            #website = 'http://www.google.com/search?q='+searchterm+'&tbm=isch'
            website = 'https://www.google.com/search?q='+searchterm + \
                '&tbm=isch&sxsrf=ALeKk03HePLsRsysTlTBaJRXPPoW6QKjog:1589485094319&source=lnms&sa=X&ved=0ahUKEwiem7CzjbTpAhVxh-AKHeLvDdAQ_AUICigB&biw=776&bih=731&dpr=1.65'
            #website = 'https://www.bing.com/images/search?q='+searchterm
            source = requests.get(website).text
            soup = BeautifulSoup(source, 'html.parser')

            imgurl = ''
            imgcount = 0
            for i in soup.find_all('img'):
                if imgcount == 10:
                    imgurl = str(i.get('src'))
                imgcount = imgcount+1
            print(imgurl)

            # this section of the code will save the image as pic1.jpg
            response = requests.get(imgurl, stream=True)
            if not response.ok:
                print(response)

            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)
        await message.channel.send(file=discord.File('pic1.jpg'))

tokenraj = 'discordtoken'
tokengarage = 'discordtoken'
client.run(tokenraj)
