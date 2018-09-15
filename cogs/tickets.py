import discord
import sqlite3
from cogs.utils import funcs
from discord.ext import commands
class tickets():
    def __init__(self, bot):
        self.bot = bot
        self.database = bot.database
    @commands.command(pass_context=True)
    async def tickets(self, arg=None):
        """Prints open tickets, nothing more nothing less."""
        if arg == None or "Open" or "open":
            result = funcs.list_open(self.database)
            print(result)
            await self.bot.say(result)
        elif arg == "Closed" or "closed":
            result = funcs.list_closed(self.database)
            print(result)
            await self.bot.say(result)
        elif arg == "Picked" or "picked":
            result = funcs.list_picked(self.database)
            print(result)
            await self.bot.say(result)
    @commands.command(hidden=True)
    async def tickets_test(self):
        conn = sqlite3.connect(self.database)
        c = conn.cursor()
        for row in c.execute('SELECT * FROM tickets'):
            print(row)
            await self.bot.say(row)
    @commands.command(pass_context=True)
    async def pick(self, ctx, id):
        moderator = ctx.message.author
        funcs.pick_logic(self.database, (moderator.id, moderator.name, id))
    @commands.command(pass_context=True)
    async def open(self, ctx, *, message):
        """Opens a support ticket, you'll be notified when a moderator accepts it."""
        member = ctx.message.author
        await self.bot.say("```{}``` will be opened as a ticket, thank you for alerting staff!".format(message))
        funcs.post(self.database, member.id, member.name, message)
    @commands.command(pass_context=True)
    @commands.has_permissions(kick_members=True)
    async def close(ctx, *, id, Reason):
        """Allows moderator to close ticket"""
        await self.bot.say("Closing ticket {}".format(Reason))
        funcs.close(id, Reason)
def setup(bot):
    bot.add_cog(tickets(bot))