#I will edit this
@bot.command()
async def highFive(ctx,name):
  await ctx.send(f'You give {name} a high five!')

def ManURL(rl):
    url = rl
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')
def getLinked(parent):
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
  soup = ManURL(url)
  #insert getting just whats suppose to be the results here, if you can get that working.
  links=getLinked(soup)
  for link in links.copy():
    if re.findall("google",link) or not re.findall("http.*:",link):
      links.remove(link)
  for num in range(0,len(links)):
    links[num]=links[num].removeprefix("/url?q=")
    links[num]=re.findall("(.+)&sa=U&ved=",links[num])[0]
  await ctx.send(links[entry])