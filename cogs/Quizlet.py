import requests
import discord
import asyncio 
import os
from discord.ext import commands


class Quizlet:
	def __init__(self,bot):
		self.bot = bot
	@commands.command(pass_context=True)
	async def quizlet(self, ctx, *search_object):
		client_id =  os.environ['CLIENT_ID']
		try:
			output = ''
			for word in search_object:
				output += word
				output += ' '
			o2 = ''
			for word in search_object:
				o2 += word
				o2 += '-'

			#Making the API Request
			url = 'https://api.quizlet.com/2.0/search/universal?q=' + str(output) +'&per_page=50'+ '&client_id='+str(client_id)
			await self.bot.say('URL Created')
			r = requests.get(url)
			data = r.json()
			vals = data['items']
			results_count = data['total_results']
			
			sug = 'https://quizlet.com/subject/' + str(o2) + '/'
			#Creating the discord embed
			embed = discord.Embed(title='**Some results related to {}**'.format(output), description='More can be found at: {}'.format(sug), color=0x000080)
			embed.add_field(name='Classes and Sets:', value='found {} results, *not all can be listed here*'.format(results_count), inline=False)
			embed.set_thumbnail(url=ctx.message.author.avatar_url)
			embed.set_footer(text='• These are just values from the first page of API returned data, most of them can be just classes or "Groups" try using "quizlet_set" command!')
			for i in vals:
			    if i['type'] != 'user':
			    	#Addning the field 
			        embed.add_field(name="{}".format(i['type'].title()), value=str('[Click Here]'+str('('+i['url']+')')) , inline=False)
			await self.bot.say("Sent to DMs")
			await self.bot.add_reaction(ctx.message,':Dms:480775527179878400')
			await self.bot.send_message(ctx.message.author,embed=embed)
		except Exception as e:
			await self.bot.say("An error occurred. Error report sent.")
			#Sends error.
			ch = self.bot.get_channel(str(479431960234819614))
			await self.bot.send_message(ch, "An error occurred. Error: **"+str(e)+"** \n \n Message: ```"+str(ctx.message.content)+'```')
#:
	@commands.command(pass_context=True, aliases=['qset'])
	async def quizlet_set(self, ctx, *search_object):
		
		try:
			output = ''
			for word in search_object:
				output += word
				output += ' '
			o2 = ''
			for word in search_object:
				o2 += word
				o2 += '-'

			
			url = 'https://api.quizlet.com/2.0/search/sets?q=' +str(output)+ '&client_id='+str(client_id)
			#print(url)
			r = requests.get(url)
			data = r.json()
			vals = data['sets']
			results_count = data['total_results']
			sug = 'https://quizlet.com/subject/' + str(o2) + '/'
			embed = discord.Embed(title='**Some results related to {}**'.format(output), description='More can be found on {}'.format(sug), color=0x000080)
			embed.set_thumbnail(url=ctx.message.author.avatar_url)
			embed.add_field(name='Sets:', value='found {} results, *not all can be listed here*'.format(results_count), inline=False)
			#Asking API for the values
			for i in vals:
				embed.add_field(name='{} with {} terms'.format(i['title'].capitalize(), i['term_count']), value=str('[Click Here]'+str('('+i['url']+')')), inline=False)
			await self.bot.say("Sent to DMs")
			await self.bot.add_reaction(ctx.message,':Dms:480775527179878400')
			await self.bot.send_message(ctx.message.author,embed=embed)
		except Exception as e:
			await self.bot.say("An error occurred. Error report sent.")
			#send the error to  my server...
			ch = self.bot.get_channel(str(479431960234819614))
			await self.bot.send_message(ch, "An error occurred. Error: **"+str(e)+"** \n \n Message: ```"+str(ctx.message.content)+'```')



def setup(bot):
	bot.add_cog(Quizlet(bot))
