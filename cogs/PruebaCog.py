# main.py
from discord.ext import commands
import os

client = commands.Bot(command_prefix = "!")

for f in os.listdir("./cogs"):
	if f.endswith(".py"):
	    client.load_extension("cogs." + f[:-3])



client.run("OTAwNTIyNzY5NTYzOTM0NzQw.YXCjLw.GkBZby_RSP-lkfNtO612hC5cPg4")