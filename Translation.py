import requests
import discord
import asyncio 
import os
from discord.ext import commands

class Translation:
	def __init__(self,bot):
		self.bot = bot
	
	@commands.command(pass_context=True)
	async def translate(self, ctx, lang_code,*text):
		output = ''
		for word in text:
			output += word
			output += ' '
		await self.bot.say("***Please wait. Requesting API values***")
		key_2 = os.environ['KEY_2']
		url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?key='+str(key_2)+'&text='+str(output)+'&lang='+str(lang_code)
		print(url)
		try:
			r = requests.post(url)
			data = r.json()
			embed = discord.Embed(title='Powerd By Yandex Translate', description=data['lang'],url='https://translate.yandex.net/', color=0x000080)
			embed.add_field(name='Text to translate: ',value='```'+output+'```', inline=False)
			embed.add_field(name='Translated Text: ', value='```'+str(data['text'][0])+'```', inline=False)
			embed.set_footer(text='Requested by: '+str(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
			
			T_msg = await self.bot.say(embed=embed)
			await self.bot.add_reaction(message=T_msg, emoji=':Correct:478556422020268048')
			await self.bot.add_reaction(message=T_msg, emoji= ':Incorrect:478556421814747147')
		except Exception as e:
			await self.bot.say("An error occurred. Error report sent.")
			ch = self.bot.get_channel(str(479431960234819614))
			await self.bot.send_message(ch, "An error occurred. Error: **"+str(e)+"** \n \n Message: ```"+str(ctx.message.content)+'```')

	@commands.command(pass_context=True)
	async def ISOs(self,ctx):
	await self.bot.send_message(ctx.message.author,'''***af   Afrikaans***\n'''+'''***am   Amharic***\n'''+'''***ar   Arabic***\n'''+'''***az   Azerbaijani***\n'''+'''***ba   Bashkir***\n'''+'''***be   Belarusian***\n'''+'''***bg   Bulgarian***\n'''+'''***bn   Bengali***\n'''+'''***bs   Bosnian***\n'''+'''***ca   Catalan***\n'''+'''***ceb   Cebuano***\n'''+'''***cs   Czech***\n'''+'''***cy   Welsh***\n'''+'''***da   Danish***\n'''+'''***de   German***\n'''+'''***el   Greek***\n'''+'''***en   English***\n'''+'''***eo   Esperanto***\n'''+'''***es   Spanish***\n'''+'''***et   Estonian***\n'''+'''***eu   Basque***\n'''+'''***fa   Persian***\n'''+'''***fi   Finnish***\n'''+'''***fr   French***\n'''+'''***ga   Irish***\n'''+'''***gd   Scottish Gaelic***\n'''+'''***gl   Galician***\n'''+'''***gu   Gujarati***\n'''+'''***he   Hebrew***\n'''+'''***hi   Hindi***\n'''+'''***hr   Croatian***\n'''+'''***ht   Haitian***\n'''+'''***hu   Hungarian***\n'''+'''***hy   Armenian***\n'''+'''***id   Indonesian***\n'''+'''***is   Icelandic***\n'''+'''***it   Italian***\n'''+'''***ja   Japanese***\n'''+'''***jv   Javanese***\n'''+'''***ka   Georgian***\n'''+'''***kk   Kazakh***\n'''+'''***km   Khmer***\n'''+'''***kn   Kannada***\n'''+'''***ko   Korean***\n'''+'''***ky   Kyrgyz***\n'''+'''***la   Latin***\n'''+'''***lb   Luxembourgish***\n'''+'''***lo   Lao***\n'''+'''***lt   Lithuanian***\n'''+'''***lv   Latvian***\n'''+'''***mg   Malagasy***\n'''+'''***mhr   Mari***\n'''+'''***mi   Maori***\n'''+'''***mk   Macedonian***\n'''+'''***ml   Malayalam***\n'''+'''***mn   Mongolian***\n'''+'''***mr   Marathi***\n'''+'''***mrj   Hill Mari***\n'''+'''***ms   Malay***\n'''+'''***mt   Maltese***\n'''+'''***my   Burmese***\n'''+'''***ne   Nepali***\n'''+'''***nl   Dutch***\n'''+'''***no   Norwegian***\n'''+'''***pa   Punjabi***\n'''+'''***pap   Papiamento***\n'''+'''***pl   Polish***\n'''+'''***pt   Portuguese***\n'''+'''***ro   Romanian***\n'''+'''***ru   Russian***\n'''+'''***si   Sinhalese***\n'''+'''***sk   Slovak***\n'''+'''***sl   Slovenian***\n'''+'''***sq   Albanian***\n'''+'''***sr   Serbian***\n'''+'''***su   Sundanese***\n'''+'''***sv   Swedish***\n'''+'''***sw   Swahili***\n'''+'''***ta   Tamil***\n'''+'''***te   Telugu***\n'''+'''***tg   Tajik***\n'''+'''***th   Thai***\n'''+'''***tl   Tagalog***\n'''+'''***tr   Turkish***\n'''+'''***tt   Tatar***\n'''+'''***udm   Udmurt***\n'''+'''***uk   Ukrainian***\n'''+'''***ur   Urdu***\n'''+'''***uz   Uzbek***\n'''+'''***vi   Vietnamese***\n'''+'''***xh   Xhosa***\n'''+
		'''***yi   Yiddish***\n'''+'''***zh   Chinese***\n''')
def setup(bot):
	bot.add_cog(Translation(bot))
