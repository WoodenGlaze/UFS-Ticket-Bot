import discord
from discord.ext import commands

class administrative:
	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True, name="kick")
	@commands.has_permissions(kick_members=True)
	async def _kick(self, ctx, mem:discord.Member):
		await self.bot.kick(mem)
		await self.bot.say('Member: {0.name} was kicked'.format(mem))

def setup(bot):
	bot.add_cog(administrative(bot))
