import requests
import discord
import asyncio
import os 
from discord.ext import commands
from aylienapiclient import textapi


Id_1 = os.environ['ID_1']
Key_1 = os.environ['KEY_1']

clinet = client = textapi.Client(Id_1, Key_1)
class Misc():
	def __init__(self,bot):
		self.bot = bot
	@commands.command(pass_context=True)
	async def bookinfo(self, ctx, *search):
		try:
			output = ''
			for word in search:
				output += word
				output += ' '
			url = 'https://www.googleapis.com/books/v1/volumes?q='+str(output)
			r = requests.get(url)
			data = r.json()
			title = data['items'][0]['volumeInfo']['title']
			auth = data['items'][0]['volumeInfo']['authors'][0]
			desc = data['items'][0]['volumeInfo']['description']
			try:
				publisher = data['items'][0]['volumeInfo']['publisher']
			except:
				publisher = 'Unknown'
			try:
				published = data['items'][0]['volumeInfo']['publishedDate']
			except:
				published = 'Not Found'
			try:
				img = data['items'][0]['volumeInfo']['imageLinks']['thumbnail']
			except:
				img = 'https://cdn.discordapp.com/attachments/472429049809993739/476045014976430084/icons8-question-mark-100.png'
			
			try:
				rating = data['items'][0]['volumeInfo']['averageRating']
			except:
				rating = 'Not Found'
			try:
				pages = data['items'][0]['volumeInfo']['pageCount']
			except:
				pages = 'Not Found'


			embed = discord.Embed(title='***'+str(title)+'***', description='By: '+auth, color=0x000080)
			embed.add_field(name='Description: ', value=str(desc), inline=True)
			embed.add_field(name='Publisher: ', value=str(publisher), inline=True)
			embed.add_field(name='Published: ', value=str(published), inline=True)
			embed.add_field(name='* Ratings'+ '(*on Google Play*): ', value=str(rating), inline=True)
			embed.add_field(name='* Page Count: ', value=str(pages), inline=True)
			embed.set_thumbnail(url=img)
			embed.set_footer(text='* Data may not be vaild.')
			await self.bot.say(embed=embed)
		except Exception as e:
			await self.bot.say('An error occurred. Error report sent.')
			ch = self.bot.get_channel(str(479431960234819614))
			await self.bot.send_message(ch, "An error occurred. Error: "+str(e))
	@commands.command(pass_context=True, aliases=['rpoem'])
	async def random_poem(self, ctx):
		try:
			r = requests.get('https://www.poemist.com/api/v1/randompoems').json
			embed = discord.Embed(name='**_'+r[0]['title']+'_**', description='By: '+r[0]['poet']['name'],url=r[0]['url'], color=0x000080)
			embed.add_field(name='Poem: ', value=r[0]['content'], inline=False)
			await self.bot.say(embed=embed)
		except Exception as e:
			await self.bot.say('An error occurred. Error report sent.')
			ch = self.bot.get_channel(str(479431960234819614))
			await self.bot.send_message(ch, "An error occurred. try again..Error: "+str(e))
	
	spoilers=[{'name': 'To Kill A Mockingbird', 'val': 'Boo kills Bob. '}, 
		{'name': 'Romeo and Juliet', 'val': 'They both die, Some were pardoned and some were punished.'},
		{'name': 'The Five People You Meet in Heaven', 'val': "Don't worry the little girls alive!"},
		{'name': 'Of Mice and Men', 'val': 'A friend kills a friend, that was the end....Bye Lennie'},
		{'name':'Give Me Your Hand','val':"Her's Secret - She killed her father"},
		{'name':'Charlotte Walsh Likes to Win by Jo Piazza','val':"Don't know who wins."},
		{'name':'Rebecca','val':'Someone was murdered.'},
		{'name':'Harry Potter and the Deathly Hallows ','val':' Ms. Rowling, you’ve tricked us again.'},
		{'name':'Death Cure','val':'The girl falls to her death...'},
		{'name':'True Memoirs of an International Assassin','val':' Nahh dont wanna spoil this one, watch da movie'},
		{'name':'Harry potter and the Sorcerers Stone','val':'Voldemort is the rapey professor.'}
		]
	@commands.command(pass_context=True, aliases=['rs', 'rspoiler'])
	async def random_spoiler(self, ctx):
		r = random.choice(spoilers)
		embed = discord.Embed(title='A ranodm spoiler', description='Dont blame me for injuries',color=0x000080)
		embed.add_field(name='{}'.format(r['name']), value=r['val'], inline=False)
		embed.set_footer(text='Dont blame me for injuries....')
		await self.bot.send_message(ctx.message.author, embed=embed)




	@commands.command(pass_context=True)
	async def suggest(self, ctx, *suggestion):
		try:
			output = ''
			for word in suggestion:
				output += word
				output += ' '
			ch = self.bot.get_channel(str(482574825991176194))
			embed = discord.Embed(title='New suggestion!', description='From {}'.format(str(ctx.message.author.name)), color=0x000080)
			embed.add_field(name='Suggestion: ', value='{}'.format(str(output)))
			await self.bot.add_reaction(message=ctx.message,emoji=':Correct1:480775087499247617')
			await self.bot.send_message(ch, embed=embed)
		except:
			await self.bot.say("Error")
			
			
def setup(bot):
	bot.add_cog(Misc(bot))
