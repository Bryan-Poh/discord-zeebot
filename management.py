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

class Management:
	def __init__(self, bot):
		self.client = bot

	minutes = 0
	hour = 0


	@commands.command(pass_context=True, no_pm=True)
	async def kick(self, ctx, user: discord.Member):
		if ctx.message.author.server_permissions.administrator:
		    embed = discord.Embed(
		        title=":boot: Goodbye {0},You are now kicked from the server!".format(user.name.mention),
		        color = discord.Colour.red()
		    )
		    await self.client.kick(user)
		    await self.client.say(embed=embed)  
		else:
			await self.client.say("You have insufficient permissions to do this command")


	@commands.command(pass_context=True, no_pm=True)
	async def about(self, ctx):
	    embed = discord.Embed(
	        title="About ZeeBot", 
	        description="I was created on 19th June 2018 by my creator, Zandrex", 
	        color = discord.Colour.orange()
	    )
	    
	    # give info about you here
	    embed.add_field(name="Author", value="@Zandrex#9925")
	    
	    # Shows the number of servers the bot is member of.
	    embed.add_field(name="Server count", value=str(len(self.client.servers)))

	    # give users a link to invite thsi bot to their server
	    embed.add_field(name="Invite", value="[Invite link](https://discordapp.com/api/oauth2/authorize?client_id=458566846556405761&permissions=8&scope=bot)")

	    await self.client.say(embed=embed)


	@commands.command(pass_context=True, no_pm=True)
	async def ping(self, ctx):
	    channel = ctx.message.channel
	    t1 = time.perf_counter()
	    await self.client.send_typing(channel)
	    t2 = time.perf_counter()
	    embed=discord.Embed(
	    	title=None, description=':ping_pong: Pong, {}ms'.format(round((t2-t1)*1000)), 
	    	color = discord.Colour.orange()
	    )
	    await self.client.say(embed=embed)

	########### Uptime ###########
	global start_time
	start_time = datetime.datetime.now()

	# Converting uptime to string 
	def timedelta_str(self, dt):
	    days = dt.days
	    hours, r = divmod(dt.seconds, 3600)
	    minutes, sec = divmod(r, 60)

	    if minutes == 1 and sec == 1:
	        return '{0} days, {1} hours, {2} minute and {3} second.'.format(days,hours,minutes,sec)
	    elif minutes > 1 and sec == 1:
	        return '{0} days, {1} hours, {2} minutes and {3} second.'.format(days,hours,minutes,sec)
	    elif minutes == 1 and sec > 1:
	        return '{0} days, {1} hours, {2} minute and {3} seconds.'.format(days,hours,minutes,sec)
	    else:
	        return '{0} days, {1} hours, {2} minutes and {3} seconds.'.format(days,hours,minutes,sec)

	@commands.command(pass_context=True, no_pm=True)
	async def uptime(self, ctx):
	    global start_time
	    embed = discord.Embed(
	        color = discord.Colour.orange()
	    )
	    embed.add_field(name="ZeeBot has been online for ", value=self.timedelta_str(datetime.datetime.now() - start_time), inline=True)
	    await self.client.say(embed=embed)

	########### Invite ###########
	@commands.command(pass_context=True, no_pm=True)
	async def invite(self, ctx):
	    embed = discord.Embed(
	        title = "ZeeBot",
	        description = "Interested to add ZeeBot to your own server?",
	        color = 0x00ff00
	    )

	    embed.add_field(name="Invite link :", value="[Just click me to add to your server!](https://discordapp.com/api/oauth2/authorize?client_id=458566846556405761&permissions=8&scope=bot)")
	    await self.client.say(embed=embed)

	########### User Info ###########
	@commands.command(pass_context=True, no_pm=True)
	async def userinfo(self, ctx, user:discord.Member):
	    embed = discord.Embed(
	        title="{}'s information".format(user.name),
	        description="Here is what I could find in the database.", 
	        color = discord.Colour.orange()
	    )

	    embed.add_field(name="Name", value=user.name, inline=True)
	    embed.add_field(name="ID", value=user.id, inline=True)
	    embed.add_field(name="Status", value=user.status, inline=True)
	    embed.add_field(name="Highest Role In Server", value=user.top_role)
	    embed.add_field(name="Joined server at", value=user.joined_at)
	    embed.set_thumbnail(url=user.avatar_url)
	    await self.client.say(embed=embed)

	########### Server Info ###########
	@commands.command(pass_context=True, no_pm=True)
	async def serverinfo(self, ctx):
	    embed = discord.Embed(
	        title="Found: {}'s information".format(ctx.message.server.name),
	        description="Here is what I found.",
	        color = discord.Colour.orange()
	    )

	    embed.add_field(name="Server Name", value=ctx.message.server.name, inline=True)
	    embed.add_field(name="Server ID", value=ctx.message.server.id, inline=True)
	    embed.add_field(name="Total Roles", value=len(ctx.message.server.roles))
	    embed.add_field(name="Total Members", value=len(ctx.message.server.members))
	    embed.set_thumbnail(url=ctx.message.server.icon_url)
	    await self.client.say(embed=embed)

	########### Prune ###########
	@commands.command(pass_context=True, no_pm=True)
	async def prune(self, ctx, amount=100):
	    channel = ctx.message.channel
	    messages = []
	    if ctx.message.author.server_permissions.administrator:
	        async for message in self.client.logs_from(channel, limit=int(amount) + 1):
	            messages.append(message)
	        await self.client.delete_messages(messages)
	        # await self.client.say(str(amount) + " messages were deleted.")
	        embed = discord.Embed(
	        	color=discord.Colour.red()
	        )
	        embed.add_field(name="Total Messages Deleted", value=str(amount), inline=True)
	        await self.client.say(embed=embed, delete_after=4)  
	    else:
	        await self.client.say("You have insufficient permissions to do this command")

def setup(bot):
    bot.add_cog(Management(bot))

