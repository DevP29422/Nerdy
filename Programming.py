import discord
import asyncio
import os
import requests
from discord.ext import commands

class Programming():
	def __init__(self,bot):
		self.bot = bot
	@commands.command(pass_context=True, aliases=['programming_help','phelp'])
	async def ph(self,ctx, language: str, *search):
		try:
			output = ''
			for word in search:
				output += word
				output += ' '
			url = 'https://api.stackexchange.com/2.2/search?order=desc&sort=activity&tagged='+str(language)+'&intitle='+str(output)+'&site=stackoverflow'
			r = requests.get(url)
			data = r.json()
			#print("Data recived and converted to JSON")
			items = data['items']
			embed = discord.Embed(title='Searched Stackoverflow for: '+str(output), description='Not every data can be listed here', color=0x000080)
			embed.set_thumbnail(url=ctx.message.author.avatar_url)
			for i in items:
				embed.add_field(name='{}'.format(i['title']).capitalize(), value=i['link'], inline=False)
			await self.bot.say("Sent to DMs")
			await self.bot.add_reaction(ctx.message,':Dms:480775527179878400')
			await self.bot.send_message(ctx.message.author,embed=embed)
		except Exception as e:
			await self.bot.say("An error occurred. Error report sent.")
			ch = self.bot.get_channel(str(479431960234819614))
			await self.bot.send_message(ch, "An error occurred. Error: **"+str(e)+"** \n \n Message: ```"+str(ctx.message.content)+'```')

def setup(bot):
	bot.add_cog(Programming(bot))
