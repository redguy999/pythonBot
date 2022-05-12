import nextcord
from nextcord.ext import commands
from auth import TOKEN

intents = nextcord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def hello(ctx):
  await ctx.send('hi!')


bot.run(TOKEN)
