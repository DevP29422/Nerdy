import discord
import asyncio 
import os
from discord.ext import commands


class Mod():
	def __init__(self,bot):
		self.bot = bot
	@commands.command(pass_context=True)
	@commands.has_permissions(kick_members=True)
	async def kick(self,ctx, user: discord.Member):
		await self.bot.kick(user)
		await self.bot.say(str(user.name)+"Has been kicked. \n by: "+str(ctx.message.author.name))

	@commands.command(pass_context=True)
	@commands.has_permissions(ban_members=True)
	async def ban(self, ctx, user: discord.Member):
		await self.bot.ban(user)
		await self.bot.say(str(user.name)+"Has been banned. \n by: "+str(ctx.message.author.name))
	@commands.command(pass_context=True)
	@commands.has_permissions(manage_nicknames=True)
	async def nick(self,ctx, user: discord.Member, *name):
		new_name = ''
		for word in name:
			new_name += word
			new_name += ' '	
		await self.bot.change_nickname(user, new_name)
		await self.bot.add_reaction(message=ctx.message, emoji=':Correct1:480775087499247617')
	@commands.command(pass_context=True)
	@commands.has_permissions(manage_messages=True)
	async def warn(self, ctx,user:discord.Member, *warning):
		try:
			warning1 = ''
			for word in warning:
				warning1 += word
				warning1 += ' '
			print(warning1)
			embed = discord.Embed(title='WARNING!', description='From: {}'.format(str(ctx.message.author.name)), color=0x000080)
			embed.add_field(name='Warning Note: ', value=str(warning1), inline=False)
			await self.bot.send_message(user,embed=embed)
			await self.bot.add_reaction(message=ctx.message, emoji=':Correct1:480775087499247617')
		except:
			await self.bot.say("An error occurred.")

	@commands.command(pass_context=True)
	@commands.has_permissions(manage_messages=True)
	async def purge(self, ctx, channel:discord.Channel, amount:int):
		deleted = await self.bot.purge_from(channel, limit=amount)
		await self.bot.say('Deleted {} message(s)'.format(len(deleted)))


def setup(bot):
	bot.add_cog(Mod(bot))