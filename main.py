import nextcord
from nextcord.ext import commands
from auth import TOKEN

intents = nextcord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def hello(ctx):
  await ctx.send('hi!')

@bot.command()
async def bye(ctx):
  await ctx.send('bye.')

@bot.command()
async def money(ctx,amount):
  await ctx.send(f'You have ${amount}')
  
@bot.command()
async def Fuck you(ctx):
  await ctx.send('fuck you too')

bot.run(TOKEN)
