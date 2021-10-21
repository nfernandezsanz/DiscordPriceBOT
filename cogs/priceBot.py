from discord.ext import commands

import sys
sys.path.append('./')
from coins import *


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

class Test(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('------')
        self.loop.create_task(update_task(self, "coin"))

def setup(client):
    client.add_cog(Test(client))