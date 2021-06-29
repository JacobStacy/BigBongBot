# bot.py

import asyncio
from discord import channel
from discord.ext.commands import Bot
from datetime import datetime
import discord
from discord.player import FFmpegPCMAudio


bot = Bot(command_prefix='!')
TOKEN = 'ODU4NzQ5NjA4Mzg5MTE1OTE0.YNiq5Q.TMNqdIWpLVN6jQcjDk_8ZT0v-ms'

@bot.event 
async def on_ready(): #Sets up bot and reports to console
	print(f'Bot connected as {bot.user}')
	await bot.change_presence(activity = discord.Activity(
		type = discord.ActivityType.watching,
		name = 'you :)'))

	await checkTime()
	

async def sendBong(hour):
	for guild in bot.guilds:

		prev = None
		prev_size = 0
		
		for channel in guild.voice_channels:
			if len(channel.members) >= prev_size:
				prev = channel
				prev_size = len(channel.members)
			
		if prev_size > 0 :
			vc = await prev.connect()
		
			vc.play(FFmpegPCMAudio("Startup.mp3",))
			await asyncio.sleep(21.994) # length of auto clip

			if hour < 12:
				for i in range((hour - 1)):
					vc.play(FFmpegPCMAudio("Bong.mp3"))
					await asyncio.sleep(2.718) # length of auto clip
			else:
				for i in range((hour - 13)):
					vc.play(FFmpegPCMAudio("Bong.mp3"))
					await asyncio.sleep(2.718) # length of auto clip
		
			vc.play(FFmpegPCMAudio("LastBong.mp3"))
			await asyncio.sleep(18.574) # length of auto clip
			
			await vc.disconnect()

			await bot.get_channel(859570392402493461).send("Bonged in '" + guild.name  + "' in the channel '" + channel.name + "' " + datetime.now().strftime("%H:%M:%S"))

		else:
			if hour < 12:
				await guild.text_channels[-1].send("Bong " * hour)
			else:
				await guild.text_channels[-1].send("Bong " * (hour-12))



async def checkTime():
	while 1:
		now = datetime.now()

		current_time = now.strftime("%H:%M:%S")
		hour = int(now.strftime("%H"))
		print("Current Time =", current_time)

		if(current_time[3:] == '00:00'):  # check if matches with the desired time
			await sendBong(hour)
		await asyncio.sleep(1) # task runs every 60 seconds


@bot.command(name='bong')
async def manBong(ctx):
	now = datetime.now()
	hour = int(now.strftime("%H"))
	await sendBong(hour)


bot.run(TOKEN)