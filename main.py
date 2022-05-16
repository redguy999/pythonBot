import nextcord
from nextcord.ext import commands
from auth import TOKEN
from datetime import time

intents = nextcord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)
#Edward edits this.
@bot.command()
async def hello(ctx):
  await ctx.send('hi!')

@bot.command()
async def bye(ctx):
  await ctx.send('bye.')
  
@bot.command()
async def date(ctx):
  today = date.today()
  await ctx.send(f"Today's date is {today}")

@bot.command()
async def money(ctx,amount):
  await ctx.send(f'You have ${amount}')

exec(open("commands.py","r").read())
exec(open("commands2.py","r").read())

bot.run(TOKEN)
