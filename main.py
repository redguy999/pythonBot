import nextcord
import beautifulsoup4
import requests
from nextcord.ext import commands
from pkg_resources import register_finder
from auth import TOKEN
from datetime import datetime, time
import re

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
  timed = str(datetime.today())
  today = datetime.strptime(timed, '%Y-%m-%d %H:%M:%S.%f')
  await ctx.send(f"Today's date is {str(today.date())}")

@bot.command()
async def money(ctx,amount):
  await ctx.send(f'You have ${amount}')

exec(open("commands.py","r").read())
exec(open("commands2.py","r").read())

bot.run(TOKEN)
