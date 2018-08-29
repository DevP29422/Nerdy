import discord
import os
import asyncio
from discord.ext import commands
from datetime import datetime
bot = commands.Bot(command_prefix = '?')
bot.launch_time = datetime.utcnow()
bot.version = 'PUBLIC 0.1.0'
''''development version 0.8.5, the first digit of that update means a major update, 
the second degit means a cog added, the third digit is when more than cogs are modified and debugged...'''


exts = ['cogs.Quizlet','cogs.English','cogs.Translation', 'cogs.Wolfram', 'cogs.Misc', 'cogs.Programming', 'cogs.Help', 'cogs.Mod']

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name=' on the web | ?help' ), 
    	status=discord.Status('online'),afk=False)
    ch1 = bot.get_channel(str(484388243400294411))
    await bot.send_message(ch1, "Bot Up!!"+str(bot.user.name))

if __name__ == '__main__':
	for exten in exts:
		bot.load_extension(exten)
		print("Loaded {}".format(exten))
  
bot.list1 = []
@bot.event
async def on_reaction_add(reaction, user):
	print(reaction.emoji)
	my_Ch = bot.get_channel(str(477233519664431115))
	await bot.send_message(my_Ch, "reaction event called")

	if str(reaction.emoji) == '<:Correct:478556422020268048>':
		hun = int(100)
		bot.list1.append(hun)
		print(bot.list1)

	elif str(reaction.emoji) == '<:Incorrect:478556421814747147>':
		zer = int(0)
		bot.list1.append(zer)
		print(bot.list1)

bot.com = 0
@bot.event
async def on_command(command, ctx):
    bot.com += 1

@bot.command(pass_context=True)
async def change_com(ctx, amt:int ):
	if str(ctx.message.channel.id) != str(481963025377787904):
		await bot.say("Can't use the command here.")
	else:
		await bot.say("Bot com is now: "+str(bot.com)+"...")
		my_Ch = bot.get_channel(str(477233519664431115))
		await bot.send_message(my_Ch, str(ctx.message.author.name)+"Used changed commands command, which is now: "+str(bot.com))

@bot.command(pass_context=True)
async def shut_down(ctx, shut_code: str):
	if str(ctx.message.author.id) == str(314858630417612801):
		ch1 = bot.get_channel(str(484388243400294411))
		await bot.send_message(ch1, "Bot is about shut down user: {}".format(ctx.message.author.name))
		await bot.close()
	else:
		await bot.say("You cannot shut down the bot...")
		ch1 = bot.get_channel(str(484388243400294411))
		await bot.send_message(ch1, "A random user {} has tried to shut down the bot".format(ctx.message.author.name))


bot.news = 'No News! :('
@bot.command(pass_context=True)
async def set_news(ctx, *news):
	if str(ctx.message.author.id) == str(314858630417612801):
		output = ''
		for word in news:
			output += word
			output += ' '
		bot.news=output
	else:
		await bot.say('You cannot use the command here.')


@bot.command(pass_context=True)
async def info(ctx):
	embed = discord.Embed(title='***Nerdy***',description='A discord bot that tries to make your school related wrok easier but mostly fails. lol. Yeah you should suggest me a better description from ?suggest', color=0x000080)
	embed.add_field(name='• In servers: ',value=len(bot.servers), inline=True)
	embed.add_field(name='• Members:  ', value=str(len(set(bot.get_all_members()))), inline=True)
	delta_uptime = datetime.utcnow() - bot.launch_time
	hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
	minutes, seconds = divmod(remainder, 60)
	days, hours = divmod(hours, 24)
	bot.up_1 = (f"{days}d, {hours}h, {minutes}m, {seconds}s")


	embed.add_field(name='• Bot Uptime: ',value=bot.up_1, inline=True)
	
	embed.add_field(name='• Commands used: ', value=str(bot.com), inline=True)
	try:
		res = str(str(sum(bot.list1)/len(bot.list1))+'%')
	except:
		res = 'N/A'
	embed.add_field(name='• Average accurate translations(after last reset): ', value=res, inline=True)
	embed.add_field(name='• Inivte Link: ', value='[Click Here](https://discordapp.com/api/oauth2/authorize?client_id=483310328009064469&permissions=8&scope=bot)', inline=True)
	embed.add_field(name='• Created using:', value='[Python(version 3.6.5)](https://www.python.org/) and [Discord.py (version 0.16.12)](https://github.com/Rapptz/discord.py)')
	

	embed.add_field(name='• Sites and APIs used: ', value='[Quizlet API](https://quizlet.com/) \n  [Google Books API](https://books.google.com/) \n [Yandex Translate API](https://translate.yandex.com/) \n [Stackoverflow API](https://stackoverflow.com/)'
		+'\n [Urban Dictionary API](https://www.urbandictionary.com/) \n [Oxford Dictionary API](https://www.oxforddictionaries.com/)'
		+ '\n [Wolfram API](https://www.wolframalpha.com/) \n [AYLIEN API](https://aylien.com/) \n[Icons8](https://icons8.com/) ' 
		, inline=True)
	
	embed.add_field(name='• Latest news/updates: ', value=bot.news, inline=True)
	
	embed.set_footer(text='Running version '+str(bot.version)+'! Requested by'+str(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
	embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/461188858688700438/478609733700288512/icons8-workspace-512.png')
	await bot.say(embed=embed)


token =  os.environ['BOT_TOKEN']
bot.run(token)
