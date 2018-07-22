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

class Music:
    def __init__(self, bot):
        self.client = bot

    youtube_dl_options = {
    'source_address': '0.0.0.0',
    'format': 'best',
    'extractaudio': True,
    'audioformat': "mp3",
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'quiet': True,
    'no_warnings': True,
    'outtmpl': "data/audio/cache/%(id)s",
    'default_search': 'auto',
    'encoding': 'utf-8',
    'default_search': 'auto',
    }

    players = {} 
    queues = {}

    def check_queue(id):
        if queues[id] != []:
            player = queues[id].pop(0)
            players[id] = player
            player.start()

    def convert_timedelta(duration):
        days, seconds = duration.days, duration.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = (seconds % 60)
        return days, hours, minutes, seco

    @commands.command(pass_context=True, no_pm=True)
    async def playurl(self, ctx, url):
        youtube_dl_options = {
            'source_address': '0.0.0.0',
            'format': 'best',
            'extractaudio': True,
            'audioformat': "mp3",
            'nocheckcertificate': True,
            'ignoreerrors': False,
            'quiet': True,
            'no_warnings': True,
            'outtmpl': "data/audio/cache/%(id)s",
            'default_search': 'auto',
            'encoding': 'utf-8',
            'default_search': 'auto',
        }
        with youtube_dl.YoutubeDL(youtube_dl_options) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            video_url = info_dict.get("url", None)
            video_id = info_dict.get("id", None)
            video_title = info_dict.get('title', None)
            video_duration = info_dict.get('duration', None)

        server = ctx.message.server
        channel = ctx.message.author.voice.voice_channel

        if ctx.message.author.voice.voice_channel:
            await self.client.join_voice_channel(channel)
        else:
            return await self.client.say("I am not connected to a voice channel! Join a voice channel and try again!")

        # await self.client.join_voice_channel(channel)
        voice_client = self.client.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
        # players[server.id] = player

        await self.client.say("Playing : `{}` Duration : `[{}]`".format(video_title, str(datetime.timedelta(seconds=video_duration))))


        player.start()
    @commands.command(pass_context=True, no_pm=True)
    async def play(self, ctx, *, song : str):
        youtube_dl_options = {
        'source_address': '0.0.0.0',
        'format': 'best',
        'extractaudio': True,
        'audioformat': "mp3",
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'quiet': True,
        'no_warnings': True,
        'outtmpl': "data/audio/cache/%(id)s",
        'default_search': 'auto',
        'encoding': 'utf-8',
        'default_search': 'auto',
        }
        with youtube_dl.YoutubeDL(youtube_dl_options) as ydl:
            info_dict = ydl.extract_info(song, download=False)
            video_url = info_dict.get("url", None)
            video_id = info_dict.get("id", None)
            video_title = info_dict.get('title', None)
            video_duration = info_dict.get('duration', None)

        server = ctx.message.server
        channel = ctx.message.author.voice.voice_channel

        if ctx.message.author.voice.voice_channel:
            await self.client.join_voice_channel(channel)
        else:
            return await self.client.say("I am not connected to a voice channel! Join a voice channel and try again!")
        
        try:
            voice_client = self.client.voice_client_in(server)
            tempMsg = await self.client.send_message(ctx.message.channel, "Searching for `" + song + "`...")
            player = await voice_client.create_ytdl_player(song, ytdl_options=youtube_dl_options, after=lambda: check_queue(server.id))
            # players[server.id] = player
            
        except Exception as e:
            print("ERROR in 'play' command: " + str(e))
            fmt = ':warning: An error occurred while processing this request: ```py\n{}: {}\n```'
        else:
            # await self.client.edit_message(tempMsg, 'Added `' + str(song) + str(datetime.timedelta(seconds=video_duration)) + '` to the song queue.')
            await self.client.say("Playing : `{}` Duration : `[{}]`".format(video_title, video_duration))
            player.start()

    @commands.command(pass_context=True, no_pm=True)
    async def queue(self, ctx, *, song : str):
        youtube_dl_options = {
        'source_address': '0.0.0.0',
        'format': 'best',
        'extractaudio': True,
        'audioformat': "mp3",
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'quiet': True,
        'no_warnings': True,
        'outtmpl': "data/audio/cache/%(id)s",
        'default_search': 'auto',
        'encoding': 'utf-8',
        'default_search': 'auto',
        }
        with youtube_dl.YoutubeDL(youtube_dl_options) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            video_url = info_dict.get("url", None)
            video_id = info_dict.get("id", None)
            video_title = info_dict.get('title', None)
            video_duration = info_dict.get('duration', None)

        server = ctx.message.server
        channel = ctx.message.author.voice.voice_channel
        
        try:
            voice_client = self.client.voice_client_in(server)
            tempMsg = await self.client.send_message(ctx.message.channel, "Searching for `" + song + "`...")
            player = await voice_client.create_ytdl_player(song, ytdl_options=youtube_dl_options, after=lambda: check_queue(server.id))
            # players[server.id] = player
            
        except Exception as e:
            print("ERROR in 'play' command: " + str(e))
            fmt = ':warning: An error occurred while processing this request: ```py\n{}: {}\n```'
        else:
            if server.id in queues:
                queues[server.id].append(player)
            else:
                queues[server.id] = [player]
            await self.client.edit_message(tempMsg,"Queued : `{}` Duration : `[{}]`".format(video_title, str(datetime.timedelta(seconds=video_duration))))
            # await self.client.edit_message(tempMsg, ':notes: Added ' + str(song) + ' to the song queue.')
            player.start()


    @commands.command(pass_context=True, no_pm=True)
    async def queueurl(self, ctx, url):
        youtube_dl_options = {
            'source_address': '0.0.0.0',
            'format': 'best',
            'extractaudio': True,
            'audioformat': "mp3",
            'nocheckcertificate': True,
            'ignoreerrors': False,
            'quiet': True,
            'no_warnings': True,
            'outtmpl': "data/audio/cache/%(id)s",
            'default_search': 'auto',
            'encoding': 'utf-8',
            'default_search': 'auto',
        }
        with youtube_dl.YoutubeDL(youtube_dl_options) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            video_url = info_dict.get("url", None)
            video_id = info_dict.get("id", None)
            video_title = info_dict.get('title', None)
            video_duration = info_dict.get('duration', None)

        server = ctx.message.server
        voice_client = self.client.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))

        if server.id in queues:
            queues[server.id].append(player)
        else:
            queues[server.id] = [player]
        await self.client.say("Queued : `{}` Duration : `[{}]`".format(video_title, str(datetime.timedelta(seconds=video_duration))))


    # @commands.command(pass_context=True, no_pm=True)
    # async def volume(ctx, value : int):
    #     # if self.client.is_playing():
    #     id = ctx.message.server.id
    #     players[id].volume = value / 100
    #     await self.client.say('Set the volume to {:.0%}'.format(players.volume))

    @commands.command(pass_context=True, no_pm=True)
    async def stop(self, ctx):
        server = ctx.message.server
        voice_client = self.client.voice_client_in(server)
        await self.client.say("`Stopping all music and disconnecting`")
        await voice_client.disconnect()

    @commands.command(pass_context=True, no_pm=True)
    async def pause(self, ctx):
        id = ctx.message.server.id
        players[id].pause()

    # @commands.command(pass_context=True, no_pm=True)
    # async def stop(self, ctx):
    #     # if self.client.is_playing():
    #     id = ctx.message.server.id
    #     await self.client.say("Stopping all music and disconnecting")
    #     player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))#
    #     # players[server.id] = player#
    #     player.stop()

    #     server = ctx.message.server
    #     voice_client = self.client.voice_client_in(server)
    #     await voice_client.disconnect()
    #     # else: 
    #     #     await self.client.say("Unable to stop. No song is playing right now.")

    @commands.command(pass_context=True, no_pm=True)
    async def skip(self, ctx):
        # if self.client.is_playing():
        id = ctx.message.server.id
        await self.client.say("Skipped")
        players[id].skip()
        # else: 
        #     await self.client.say("Unable to skip. No song is playing right now.")

    @commands.command(pass_context=True, no_pm=True)
    async def resume(self, ctx):
        id = ctx.message.server.id
        players[id].resume()

def setup(bot):
    bot.add_cog(Music(bot))