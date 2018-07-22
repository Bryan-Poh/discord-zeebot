
# If code does not run, do
# "pip install discord " on cmd

import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import json
import os
import chalk
import youtube_dl
import random
import io
import aiohttp
import time
import datetime
from datetime import datetime as dt
import logging
import re
from itertools import cycle


bot_token = process.env.bot_token
prefix = ">"
bot = commands.Bot(command_prefix=prefix)
status = [">help | " + str(len(bot.servers)) + " servers", "Owner: Zandrex"]

description = "ZeeBot - Discord bot by Zandrex"

extensions = [
"helplist", 
"management", 
# "music", 
"musicplaylist",
"fun"
]

@bot.event
async def on_ready():
    print("----------------------------------------------------------")
    print("ZeeBot is now online.")
    print("Discord version: " + discord.__version__)
    print("Bot version: v1.1.0" )
    print("----------------------------------------------------------")
    print("Prefix: " + prefix)
    print("Total server count: " + str(len(bot.servers)))
    print("Running on servers: ")
    print("----------------------------------------------------------")
    # print(len(bot.servers))
    [(lambda s: print(" - %s (%s)" % (s.name, s.id)))(s) for s in bot.servers] #Prints list of server name, server id
    print("----------------------------------------------------------")
    await bot.change_presence(game=discord.Game(name=">help | " + str(len(bot.servers)) + " servers"))  

if __name__ == "__main__":
    bot.remove_command("help")
    for extension in extensions:
        try:
            bot.load_extension(extension)    
            print("Loaded cog file: [{}]".format(extension))
                
        except Exception as error:
            print("Cog file : [{}] cannot be loaded. [{}]".format(extension, error))
    print(">>> Loaded all available cog files.")
    print(">>> ATTEMPTING TO GO ONLINE...")

bot.run(bot_token)
