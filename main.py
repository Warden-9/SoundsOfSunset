# Mark Hibbing CIS 345 Tues/Thurs 12:00 - 1:15pm Project Project Submission

from lib2to3.pgen2.token import tok_name
import discord
from discord.ext import commands
import music
import json

f = open('token.json')
t = json.load(f)

cogs = [music]

client = commands.Bot(command_prefix='/', intents=discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run(t['token'])

