import asyncio
import discord
import os
from discord.ext import commands
from coins       import *
from dotenv      import load_dotenv, find_dotenv

bot1 = commands.Bot(command_prefix='#')
bot2 = commands.Bot(command_prefix='$')

#Config
load_dotenv(find_dotenv())
Token_1 = os.environ.get("Token_1")
Token_2 = os.environ.get("Token_2")


async def update_task(bot, coin):
    counter = 0
    while(True):
        counter += 1
        data  = get_coin_status('gamestarter')
        emoji = "➡️"

        if(data['Change'] < 0):
            emoji = "⏬"
        elif(data['Change'] > 0):
            emoji = "⏫"

        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name= "$" + str(data['Price']) + " " + emoji + " " + str(data['Change']) + "%"))
        await asyncio.sleep(10)

@bot1.event
async def on_ready():
    print(f'Logged in as {bot1.user} (ID: {bot1.user.id})')
    print('------')
    bot1.loop.create_task(update_task(bot1, "coin"))


@bot2.event
async def on_ready():
    print(f'Logged in as {bot2.user} (ID: {bot2.user.id})')
    print('------')
    await bot2.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="0 USD"))


# Initialize Bots
loop  = asyncio.get_event_loop()
task1 = loop.create_task(bot1.start(Token_1)) #GAME TOKEN BOT
task2 = loop.create_task(bot2.start(Token_2)) #DARK TOKEN BOT

try:
    loop.run_forever()
finally:
    loop.stop()


