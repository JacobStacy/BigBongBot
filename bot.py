# bot.py

import asyncio
from discord import client, message
from discord.ext.commands import Bot
from datetime import datetime
import discord
import threading


bot = Bot(command_prefix='!')
TOKEN = 'ODU4NzQ5NjA4Mzg5MTE1OTE0.YNiq5Q.TMNqdIWpLVN6jQcjDk_8ZT0v-ms'

@bot.event 
async def on_ready(): #Sets up bot and reports to console
	print(f'Bot connected as {bot.user}')
	await bot.change_presence(activity = discord.Activity(
		type = discord.ActivityType.watching,
		name = 'you :)'))

	await checkTime()
	


@bot.command(name='server')
async def fetchServerInfo(context):
	guild = context.guild
	
	await context.send(f'Server Name: {guild.name}')
	await context.send(f'Server Size: {len(guild.members)}')
	await context.send(f'Server Name: {guild.owner.display_name}')

async def sendBong(hour):
	for guild in bot.guilds:
			if hour < 12:
				await guild.text_channels[0].send("Bong " * hour)
			else:
				await guild.text_channels[0].send("Bong " * (hour-12))


async def checkTime():


	now = datetime.now()


	current_time = now.strftime("%H:%M:%S")
	hour = int(now.strftime("%H"))
	print("Current Time =", current_time)

	if(current_time[3:] == '00:00'):  # check if matches with the desired time
		await sendBong(hour)
	
	await asyncio.sleep(1) # task runs every 60 seconds
	await checkTime()

		



bot.run(TOKEN)