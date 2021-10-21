import asyncio
import discord

from discord.ext import commands

from pycoingecko import CoinGeckoAPI
import requests
import json



bot1 = commands.Bot(command_prefix='#')
bot2 = commands.Bot(command_prefix='$')

cg = CoinGeckoAPI()


'''
class Tracker(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.my_background_task())

    async def on_ready(self):
        print(f'Inicio de sesion como {self.user} (ID: {self.user.id})')
        print('------')

    async def my_background_task(self):
        await self.wait_until_ready()
        counter = 0
        while not self.is_closed():
            counter += 1
            await self.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= str(counter) + "USD"))
            await asyncio.sleep(60) # task runs every 60 seconds
'''
async def update_task(bot, coin):
    counter = 0
    while(True):
        counter += 1
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= str(counter) + " USD"))
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


# Inicializo los Bots
loop  = asyncio.get_event_loop()
task1 = loop.create_task(bot1.start('OTAwNTI3MDU0Mjk3MTE2NzAy.YXCnLA.g6dMryNi8IWVnWu3YsMY-_1J0NU')) #Jr
task2 = loop.create_task(bot2.start('OTAwNTIyNzY5NTYzOTM0NzQw.YXCjLw.Bwvjq3wm9bAkN5a7ecciuHA2y0o')) #Tipico

try:
    loop.run_forever()
finally:
    loop.stop()


