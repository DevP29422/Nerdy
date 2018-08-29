import requests
import discord
import os 
import asyncio 
from discord.ext import commands



class wolfram():
	def __init__(self,bot):
		self.bot = bot
	@commands.command(pass_context=True)
	async def solve(self,ctx, *problem):
		app_1 = os.environ['APP_1']
		output = ''
		for word in problem:
			output += word
		#print(output)

		try:
			url = 'http://api.wolframalpha.com/v2/query?appid='+str(app_1)+'&input=solve+'+str(output)+'&podstate=Result__Step-by-step+solution&format=plaintext&output=json'
			r = requests.get(url)
			data = r.json()
			embed = discord.Embed(title='Solved', description='Problem: '+str(output), color=0x000080)
			for i in data['queryresult']['pods']:
				for x in i['subpods']:
					#print(x['plaintext'])
					if x['plaintext'] != '':
						embed.add_field(name= i['title'],  value=x['plaintext'], inline=True)
			
			await self.bot.say("Sent to DMs")
			await self.bot.add_reaction(ctx.message,':Dms:480775527179878400')
			await self.bot.send_message(ctx.message.author,embed=embed)
		except Exception as e:
			await self.bot.say("An error occured. Error report sent.")
			ch = self.bot.get_channel(str(479431960234819614))
			await self.bot.send_message(ch, "An error occure. Error: **"+str(e)+"** \n \n Message: ```"+str(ctx.message.content)+'```')


	@commands.command(pass_context=True)
	async def quickfind(self,ctx, *search):
		app_1 = os.environ['APP_1']
		output = ''
		for word in search:
			output += word
			output += ' '
		try:
			url = 'http://api.wolframalpha.com/v1/result?appid='+str(app_1)+'&i='+str(output)
			r = requests.get(url).text
			#print(url)
			#print(r)
			if r != 'Wolfram|Alpha did not understand your input':
				await self.bot.say('**Question:**  \n {} \n \n **Answer:** \n {}'.format(str(output), str(r)))
			else:
				await self.bot.say("Failed to get results")
		except Exception as e:
			await self.bot.say("An error occurred. Error report sent.")
			
			ch = self.bot.get_channel(str(479431960234819614))
			await self.bot.send_message(ch, "An error occurred. Error: **"+str(e)+"** \n \n Message: ```"+str(ctx.message.content)+'```')

def setup(bot):
	bot.add_cog(wolfram(bot))
