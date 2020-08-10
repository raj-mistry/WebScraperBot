import discord,random
from discord.ext import commands
from PIL import Image
from io import BytesIO
import requests
from bs4 import BeautifulSoup
import urllib.request











with open('pic1.jpg', 'wb') as handle:

        searchterm = 'bucket'
        #this section of the code will take a website, and
        #grab the 10th image
        website = 'http://www.google.com/search?q='+searchterm+'&tbm=isch'
        source = requests.get(website).text
        soup = BeautifulSoup(source,'html.parser')

        imgurl = ''
        imgcount = 0
        for i in soup.find_all('img'):
            if imgcount==10:
                imgurl=str(i.get('src'))
            imgcount=imgcount+1
        print(imgurl)


        #this section of the code will save the image as pic1.jpg
        response = requests.get(imgurl, stream=True)
        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)