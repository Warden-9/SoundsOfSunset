# Mark Hibbing CIS 345 Tues/Thurs 12:00 - 1:15pm Project Project Submission

import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='/', intents=discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run("OTA5MTgyNTc5NjU4MzI2MTE3.YZAkQg.RaMqgDi3-yULTReu4wo_Smqi-FM")

