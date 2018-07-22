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

class HelpList:
    def __init__(self, bot):
        self.client = bot

    
    @commands.command(pass_context=True, no_pm=True)
    async def help(self, ctx):
        embed1 = discord.Embed(
            color = discord.Colour.orange()
        )
        embed1.add_field(name="**Management**", value="\u200b")
        # embed1.add_field(name="Commands", icon_url=author)
        embed1.add_field(name="`>invite`", value="Add ZeeBot to your servers with the invite link", inline=False)
        embed1.add_field(name="`>ping`", value="Returns Pong!", inline=False)
        embed1.add_field(name="`>userinfo @user`", value="Returns information about user!", inline=False)
        embed1.add_field(name="`>serverinfo`", value="Returns information about server!", inline=False)
        embed1.add_field(name="`>about`", value="Returns information about ZeeBot!", inline=False)
        embed1.add_field(name="`>prune [amount]`", value="Deletes [amount] of messages", inline=False)
        embed1.add_field(name="`>uptime`", value="ZeeBot's uptime", inline=False)
        embed1.add_field(name="`>kick @user`", value="Kicks user", inline=False)

        await self.client.say(embed=embed1)

        embed2 = discord.Embed(
            color = discord.Colour.orange()
        )

        embed2.add_field(name="**Music**", value="\u200b")
        # embed2.add_field(name=">playurl [url]", value="Plays music from YouTube URL", inline=False)
        # embed2.add_field(name=">play [song name]", value="Plays music from song name", inline=False)
        # embed2.add_field(name=">queueurl [url]", value="Queue a song from url", inline=False)
        # embed2.add_field(name=">queue [song name]", value="Queue a song", inline=False)
        embed2.add_field(name=">play [song name / url]", value="Plays music from song name / URL. Automatically queues song.", inline=False)
        embed2.add_field(name=">pause", value="Pause current music", inline=False)
        embed2.add_field(name=">resume", value="Resume current music", inline=False)
        embed2.add_field(name=">stop", value="Stop all music and leave from voice channel", inline=False)
        embed2.add_field(name=">skip", value="Skips song. Song requester = instant skip.", inline=False)
        embed2.add_field(name=">summon", value="Summons / move bot to voice channel", inline=False)
        embed2.add_field(name=">playing", value="Get current song information", inline=False)
        embed2.add_field(name=">volume", value="Set song volume", inline=False)

        await self.client.say(embed=embed2)

        embed3 = discord.Embed(
            color = discord.Colour.orange()
        )

        embed3.add_field(name="**Games/Fun**", value="\u200b")
        embed3.add_field(name=">8ball", value="Get your answers from the Magic 8 Ball", inline=False)
        embed3.add_field(name=">coinflip", value="Coin Flip", inline=False)
        embed3.add_field(name=">roll", value="Rolls a number from 1 to 100", inline=False)
        embed3.add_field(name=">choose", value="Chooses for you. (test, test2, test3)", inline=False)
        embed3.add_field(name=">gif [search]", value="Searches a random gif with related keyword", inline=False)

        # await self.client.send_message(author, embed=embed) #sends message to user
        await self.client.say(embed=embed3)


def setup(bot):
    bot.add_cog(HelpList(bot))

