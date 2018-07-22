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

class Fun:
    def __init__(self, bot):
        self.client = bot

    choices = [
        "It is certain :8ball:",
        "It is decidedly so :8ball:",
        "Without a doubt :8ball:",
        "Yes, definitely :8ball:",
        "You may rely on it :8ball:",
        "As I see it, yes :8ball:",
        "Most likely :8ball:",
        "Outlook good :8ball:",
        "Yes :8ball:",
        "Signs point to yes :8ball:",
        "Reply hazy try again :8ball:",
        "Ask again later :8ball:",
        "Better not tell you now :8ball:",
        "Cannot predict now :8ball:",
        "Concentrate and ask again :8ball:",
        "Don't count on it :8ball:",
        "My reply is no :8ball:",
        "My sources say no :8ball:",
        "Outlook not so good :8ball:",
        "Very doubtful :8ball:"
    ]
    @commands.command(pass_context=True, no_pm=True,name="8", aliases=["8ball"])
    async def _8ball(self, ctx):
        embed = discord.Embed(
            title="Magic 8 Ball says: ",
            color=discord.Colour.blue()
        )
        embed.add_field(name="Hmmm", value=str(random.choice(choices)), inline=True)
        await self.client.say(embed=embed)  

        # self.client.say("Magic 8 Ball says: " + random.choice(choices))

    ########### CoinFlip ###########
    @commands.command(pass_context=True, no_pm=True)
    async def coinflip(self, ctx):
        embed = discord.Embed(
            color=discord.Colour.blue()
        )
        coin = ["Heads :cd: ", "Tails :dvd: "]
        # gif = discord.Embed(title='Fliping...', color=discord.Colour.blue())
        # gif.set_image(url='https://thumbs.gfycat.com/KeenMeaslyCatbird-max-1mb.gif')
        
        # await self.client.say(embed=gif)
        # await asyncio.sleep(2.6)
        embed.add_field(name="It is", value=str(random.choice(coin)))
        await self.client.say(embed=embed)

    ########### Roll ###########
    @commands.command(pass_context=True, no_pm=True)
    async def roll(self, ctx):
        r = random.randint(1,100)

        embed = discord.Embed(
            title="Rolling from 1 to 100 ",
            color=discord.Colour.blue()
        )

        embed.add_field(name="You rolled ", value=":game_die: " + str(r) + "! :game_die:", inline=True)
        await self.client.say(embed=embed)

    ########### Choose ###########
    @commands.command(pass_context=True, no_pm=True)
    async def choose(self, ctx, *, choices: str):
        choicesList = choices.split(",")
        chosen = choicesList[random.randrange(len(choicesList))]
        await self.client.say(ctx.message.author.mention + ": I chose " + chosen + "")

    ########### Gif ###########
    @commands.command(pass_context=True, no_pm=True)
    async def gif(self, ctx, *keywords):
        """Retrieves first search result from giphy"""
        if keywords:
            keywords = "+".join(keywords)
        # else:
        #     await bot.send_cmd_help(ctx)
        #     return

        GIPHY_API_KEY = "rdA8XvF9inMBchr8wofFtBtw2gZT2XrS"

        url = ("http://api.giphy.com/v1/gifs/random?&api_key={}&tag={}".format(GIPHY_API_KEY, keywords))
        async with aiohttp.get(url) as r:
            result = await r.json()

            if r.status == 200:         
                
                if result["data"]:
                    await self.client.say(result["data"]["url"])
                else:
                    await self.client.say("No results found.")
            else:
                await self.client.say("Error contacting the API")

def setup(bot):
    bot.add_cog(Fun(bot))