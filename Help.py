import discord
import asyncio 
from discord.ext import commands

class Help():
	def __init__(self, bot):
		self.bot = bot
	@commands.command(pass_context=True)
	async def help(self,ctx, cmd='cmd'):
		embed = discord.Embed(title='Thy help has arrived.', description='...', color=0x000080)
		embed.add_field(name='English Cog:', value='?summrize <longtext>, summrizes the <longtext> given in to 4 sentences \n ' +
			'?resourceme <topic>, gets articles realted to the <topic> [aliases: `re_me`] \n' '?define <word>, gets definitions for word given from Oxford Disconary and Urban Disconary \n', 
		inline=True)
		embed.add_field(name='Misc Cog: ', value='?bookinfo <name>, gets the information about the book from Google Books. \n ?random_poem, gets a random poem [aliases=`rpoem`] \n '+
			'?suggest, sends a suggestion for the bot to the suggestions channel.', inline=True)
		embed.add_field(name='Mod Cog: ', value='?kick <user>, kicks the user (must have kick perms) \n ?ban <user>, bans a user (must have ban perms)'+
			'?nick <user> <new_name>, changes a users nick name (must have manage messages nicknames)\n ?warn <user> <warning>, warns the user with a message (must have manage messages perms). \n ?purge <channel> <amt>, deletes <amt> messages from the <channel> (must have manage messages perms)',
			inline=True)
		embed.add_field(name='Programming Cog: ', value='?ph <language> <query>, searched Stackoverflow for <query> [aliases=`phelp, programming_help`]', inline=True)
		embed.add_field(name='Quizlet Cog: ', value='?quizlet <query>, searches quizlet for <query> \n  ?quizlet_set, searches quizlet sets for <query> ', inline=True)
		embed.add_field(name='Translation Cog: ', value='?translate <lang_Code> <text>, translate <text> to given <lang_Code> \n ?ISOs, gets you ISO codes for available languages', inline=True)
		embed.set_thumbnail(url=ctx.message.author.avatar_url)
		await self.bot.say(embed=embed)

def setup(bot):
	bot.remove_command("help")
	bot.add_cog(Help(bot))
