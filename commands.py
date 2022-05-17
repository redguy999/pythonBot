#I will edit this
@bot.command()
async def highFive(ctx,name):
  await ctx.send(f'You give {name} a high five!')

def ManURL(rl):
    url = rl
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')
def getLinked():
    tags = soup.find_all('a')
    linksFound = []
    for x in tags:
      linksFound.append(x['href'])
    return linksFound

@bot.command()
async def search(ctx,term,entry):
  try:
    entry=int(entry)
  except:
    entry=0
  #id=rcnt
  #search "term" on google, and return the url of the result matching the entry number.
  url=f"https://www.google.com/search?q={term}"
  global soup
  soup = soup.find(id="rcnt")
  soup = ManURL(url)
  giveBack=getLinked()[entry]
  await ctx.send(giveBack)