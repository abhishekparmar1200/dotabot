import discord
import pandas
import os
import pandas as pd
from discord.ext import commands

df=pd.read_json("weakness.json")
del(df[''])

client = discord.Client()  

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event



async def on_message(message):
    if message.author == client.user:
        return
    suggest=[]
    if message.content.startswith('$help_dio'):
        #for i in range(0,30):
        await connect(23,false)
        #await message.channel.send("/tts fuck you kunro ", tts=True)
        #await message.channel.send(file=discord.File('tenor1.gif'))
            #await message.channel.send(file=discord.File('tenor1.gif'))
    if message.content.startswith('$suggest'):
        suggest.append(message.content)
        a=message.content
        a=a.replace("$suggest","")
        f= open("suggest.txt","w+")
        f.write(a)
        await message.channel.send("the deed is done")
    if message.content.startswith('$hari3'):
        await message.channel.send(file=discord.File('tenor1.gif'))

    if message.content.startswith('$botsal'):
        for i in range(0,5):
            await message.channel.send(file=discord.File('bot.jpg'))

    if message.content.startswith('$aja_raja'):
        v=message.content
        v=v.replace("$aja_raja","")
        for i in range(0,30):
            await message.channel.send(v)

    if message.content.startswith('$happy_birth'):
        v=message.content
        v=v.replace("$happy_birth","")
        for i in range(0,5):
            await message.channel.send(v)
        await message.channel.send(file=discord.File('birth.gif'))

    if message.content.startswith('$find_crush'):
        v=message.content
        v=v.replace("$find_crush","")
        v=v.replace(" ","")
        v=str(v)
       


        d={"<@!583659065801048095>":"Kshitij","<@!706110032185524224>":"HritikT"}
        if (d[v]=="Kshitij"):
            for j in range(0,3):
                await message.channel.send("error multiple targets found")
        elif (d[v]=="HritikT"):
            for j in range(0,3):
                await message.channel.send("Viper")
            await message.channel.send(file=discord.File("viper.jpg"))
        
    if message.content.startswith("$w"):
        v=message.content
        v=v.replace("$w ","")
        l=df[v]
        await message.channel.send(l)


client.run(Token)

