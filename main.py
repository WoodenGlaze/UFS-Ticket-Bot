import discord
import json
import youtube_dl
import logging
import os
from collections import Counter
from colorama import Fore, Back, Style, init
from discord.ext import commands
from discord.ext.commands import Bot
from cogs.utils import funcs
from datetime import datetime

database = "./main.db"

if os.name == 'nt':
	init()

if os.path.exists("init.json"):
	def loadtest():
		with open('init.json') as init:
			return json.load(init)
	values = loadtest()
	value = values['initial-run']
	if value == 1:
		print(fore.GREEN + "Initial run done.")
else:
	json_values = {
		"initial-run": "1"
	}
	funcs.create_connection(database)
	with open('init.json', 'w') as outfile:
		json.dump(json_values, outfile)

if os.path.exists("discord.log"):
	os.remove("discord.log")

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

def credload():
	with open('config.json') as f:
		return json.load(f)

initial_extensions = [
'cogs.administrative',
'cogs.tickets']

if True == True:
	credentials = credload()
	token = credentials['token']
	botowner = credentials['botowner']
	shards = credentials['shards']

desc = """Basic bot to open support tickets for the Unturned server."""
bot = Bot(command_prefix=commands.when_mentioned_or('ticket)', 'problem)'), shard_count=shards, description=desc)

bot.version = "master 0.1α"
bot.exts = initial_extensions
bot.database = database

gitversion = "WIP"


@bot.event
async def on_ready():
	print(Fore.GREEN + 'Logged in as: {0.name} [id: {0.id}]'.format(bot.user))
	print(Fore.GREEN + 'Current version: {} Latest version: {}'.format(bot.version,gitversion))
	print(Fore.GREEN + '_______')
	print(Fore.GREEN + 'Sharding: {}'.format(bot.shard_count))
	logger.info('{0.name}, {0.id}'.format(bot.user))
	bot.appinfo = await bot.application_info()
	bot.uptime = datetime.now()
	await bot.change_presence(game=discord.Game(name='Abuse of this bot is punishable by a ban from it.'), status=discord.Status.dnd)

@bot.event
async def on_resumed():
	print(Fore.RED + 'Connection lost at: {} [{}], resuming normal operations.'.format(datetime.now(), bot.realuptime))

@bot.command(server=int)
async def leave_server(hidden=True):
	await bot.leave_server(discord.Server(id=server))
@bot.command(hidden=True)
async def order227():
	channel = discord.Object(id='473729350257082370')
	await bot.send_message(channel, 'All operations seized, contact <@106423924614545408> immediatly for more information. (O-227 executed)')
@bot.command()
async def reloadall():
	for extension in initial_extensions:
		try:
			bot.unload_extension(extension)
			bot.load_extension(extension)
			await self.bot.say(":ok_hand:")
		except Exception as e:
			print(Fore.RED + 'Failed to load ext {}\n{}: {}'.format(extension, type(e).__name__, e))
@bot.command()
async def about():
	"""Tells you information about the bot itself."""
	revision = os.popen(r'git show -s HEAD --format="%s (%cr)"').read().strip()
	result = ['**About Me:**']
	result.append('- Author: Miss Glazeee~ [ID: 106423924614545408]')
	result.append('- Library: discord.py (Python)')
	result.append('- Latest Change: {}'.format(revision))
	bot.actualuptime = datetime.now() - bot.uptime
	result.append('- Uptime: {}'.format(bot.actualuptime))
	result.append('- Servers: {}'.format(len(bot.servers)))
	#result.append('- Commands Run: {}'.format(sum(bot.commands_used.values())))
	# statistics
	total_members = sum(len(s.members) for s in bot.servers)
	total_online  = sum(1 for m in bot.get_all_members() if m.status != discord.Status.offline)
	unique_members = set(bot.get_all_members())
	unique_online = sum(1 for m in unique_members if m.status != discord.Status.offline)
	channel_types = Counter(c.type for c in bot.get_all_channels())
	voice = channel_types[discord.ChannelType.voice]
	text = channel_types[discord.ChannelType.text]
	result.append('- Total Members: {} ({} online)'.format(total_members, total_online))
	result.append('- Unique Members: {} ({} online)'.format(len(unique_members), unique_online))
	result.append('- {} text channels, {} voice channels'.format(text, voice))
	result.append('')
	result.append('Unturned Furry Server: https://discord.gg/GsyRaZf')
	await bot.say('\n'.join(result))

@bot.event
async def on_member_ban(member):
	server = member.server
	logger.info('{0.name}[id: {0.id}] got banned from {1.name}[{1.id}].'.format(member, server))
	print(Fore.RED + '{0.name}[id: {0.id}] got banned from {1.name}[{1.id}].'.format(member, server))

@bot.event
async def on_server_join(server):
	print(Fore.GREEN + 'Bot joined server: {0.name}[id: {0.id}]')

if __name__ == '__main__':
	for extension in initial_extensions:
		try:
			bot.load_extension(extension)
		except Exception as e:
			print(Fore.RED + 'Failed to load ext {}\n{}: {}'.format(extension, type(e).__name__, e))

bot.run(token)
