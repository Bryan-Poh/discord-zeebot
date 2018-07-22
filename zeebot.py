
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

#Directory of zeebot for import os(lvl)
# os.chdir(r'C:\Users\18054040\Desktop\ZeeBot')
os.chdir(r'C:\Users\user\Desktop\ZeeBot')

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


# async def change_status():
#     await bot.wait_until_ready()
#     statuses = cycle(status)

#     while not bot.is_closed:
#         current_status = next(statuses)
#         await bot.change_presence(game=discord.Game(name=current_status))
#         await bot.change_presence(game=discord.Game(name=">help | " + str(len(bot.servers)) + " servers"))  
#         await asyncio.sleep(1)      

# @bot.event
# async def on_member_join(member):
#     with open('users.json', 'r') as f:
#         users = json.load(f)

#     await update_data(users, member)

#     with open('users.json', 'w') as f:
#         json.dump(users, f)

# @bot.event
# async def on_message(message):
#     with open('users.json', 'r') as f:
#         users = json.load(f)

#     await update_data(users, message.author)
#     await add_experience(users, message.author, 5)
#     await level_up(users, message.author, message.channel)

#     with open('users.json', 'w') as f:
#         json.dump(users, f)

# async def update_data(users, user):
#     if not user.id in users:
#         users[user.id] = {}
#         users[user.id]['experience'] = 0
#         users[user.id]['level'] = 1

# async def add_experience(users, user, exp):
#     users[user.id]['experience'] += exp

# async def level_up(users, user, channel):
#     experience = users[user.id]['experience']
#     lvl_start = users[user.id]['level']
#     lvl_end = int(experience ** (1/4))
    
#     if lvl_start < lvl_end:
#         await bot.send_message(channel, '{} just leveled up! Current level : {}'.format(user.mention, lvl_end))
#         users[user.id]['level'] = lvl_end

    # embed = discord.Embed(
    #     title="Level up!",
    #     color=0x00ff00
    # )

    # if lvl_start < lvl_end:

    #     embed.add_field(name="Wow!", value='{} just leveled up! Current level : {}'.format(user.mention, lvl_end), inline=True)
    #     embed.set_thumbnail(url=user.avatar_url)
    #     users[user.id]['level'] = lvl_end
    #     await bot.say(embed=embed)

# ================================================= #


# @bot.event
# async def on_member_join(member):
#     serverchannel = member.server.get_channel("channel_id")
#     message = ":wave: Welcome {0} to {1}, hope you enjoy your stay!".format(member.mention, member.server.name)
#     await bot.send_message(serverchannel, message)



# @bot.event
# async def on_member_remove(member):
#     serverchannel = member.server.get_channel("channel_id")
#     message = ":boot: Goodbye {0},You are now remove from the server!".format(member.mention)
#     await bot.send_message(serverchannel, message)

########### Kick ###########


# bot.loop.create_task(change_status())
bot.run(bot_token)