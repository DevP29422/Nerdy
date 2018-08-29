import requests
import discord
import asyncio
import os 
from discord.ext import commands
from aylienapiclient import textapi


Id_1 = os.environ['ID_1']
Key_1 = os.environ['KEY_1']

clinet = client = textapi.Client(Id_1, Key_1)
class English():
	def __init__(self, bot):
		self.bot = bot
	@commands.command(pass_context=True)
	async def summrize(self,ctx, *longtext):
		try:
			output = ''
			for word in longtext:
				output += word
				output += ' '
			s = client.Summarize({'text':str(output),'title':'Test', 'sentences_number': 4})
			print(s['sentences'])
			o2 = ''
			for i in s['sentences']:
				o2 += i
			await self.bot.say("Sent to DMs")
			await self.bot.add_reaction(ctx.message,':Dms:480775527179878400')
			await self.bot.send_message(ctx.message.author, '**Text Given**:\n '+str(output)+' \n \n **Text Summrized**: \n'+str(o2))
		except Exception as e:
			await self.bot.say("An error occurred. Error report sent.")
			ch = self.bot.get_channel(str(479431960234819614))
			await self.bot.send_message(ch, "An error occurred. Error: **"+str(e)+"** \n \n Message: ```"+str(ctx.message.content)+'```')
	@commands.command(pass_context=True, aliases=['re_me'])
	async def resourceme(self, ctx, *search):
		try:
			output = ''
			for word in search:
				output += word
				output += ' '
			key_res = os.environ['KEY_RES']
			url = 'http://api.springernature.com/metadata/json?q='+str(output)+'&api_key='+str(key_res)
			#print(url)
			r = requests.get(url)
			data = r.json()
			embed = discord.Embed(title='Resources Found', description=data['query'], color=0x000080)
			embed.set_footer(text='Use command ?resources to get websites that may help you.')
			for i in data['records']:
				embed.add_field(name=i['title'], value=str('[Click Here]'+str('('+i['url'][0]['value'])+')'), inline=False)
			await self.bot.say("Sent to DMs")
			await self.bot.add_reaction(ctx.message,':Dms:480775527179878400')
			await self.bot.send_message(ctx.message.author, embed=embed)

		except Exception as e:
			await self.bot.say("An error occurred. Error report sent.")
			ch = self.bot.get_channel(str(479431960234819614))
			await self.bot.send_message(ch, "An error occurred. Error: **"+str(e)+"** \n \n Message: ```"+str(ctx.message.content)+'```')
	@commands.command(pass_context=True)
	async def define(self, ctx, word:str):
		app_id =  os.environ['APP_ID']
		app_key = os.environ['APP_KEY']
		try:
			url = 'https://od-api.oxforddictionaries.com/api/v1/entries/en/'+str(word.lower())
			r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
			data = r.json()
			ox_definition = data['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0].capitalize()
		except:
			ox_definition = 'Not found'
		try:
			url_1 = 'http://api.urbandictionary.com/v0/define?term='+str(word.lower())
			r1 = requests.get(url_1)
			data = r1.json()
			ur_definition = str(data['list'][1]['definition'])
		except:
			ur_definition = 'Not found'
		try:
			embed = discord.Embed(title='Definition for the word: '+str(word), description='Definitions found from Oxford Dictionary  API and Urban Dictionary API', color=0x000080)
			embed.set_thumbnail(url=ctx.message.author.avatar_url)
			embed.add_field(name='Oxford Dictionary: ', value=ox_definition, inline=False)
			embed.add_field(name='Urban Dictionary: ', value=ur_definition, inline=False)
			await self.bot.say(embed=embed)
		except:
			await self.bot.say("An error occurred. Error report sent.")
			
			ch = self.bot.get_channel(str(479431960234819614))
			await self.bot.send_message(ch, "An error occurred. Error: **"+str(e)+"** \n \n Message: ```"+str(ctx.message.content)+'```')
def setup(bot):
	bot.add_cog(English(bot))
