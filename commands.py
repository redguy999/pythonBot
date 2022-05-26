#I will edit this
import nextcord
import os
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
async def search(ctx,entry,*term):
  searchTerm =""
  for word in term:
    searchTerm+=word
  try:
    entry=int(entry)
  except:
    entry=0
  #id=rcnt
  #search "term" on google, and return the url of the result matching the entry number.
  url=f"https://www.google.com/search?q={searchTerm}"
  global soup
  soup = ManURL(url)
  #insert getting just whats suppose to be the results here, if you can get that working.
  links=getLinked(soup)
  for link in links.copy():
    if re.findall("google",link) or not re.findall("http.*:",link):
      links.remove(link)
  for num in range(0,len(links)):
    try:
      links[num]=re.findall("(.+)&sa=U&ved=",links[num])[0]
    except:
      print(f"re.findall failed to work on: {links[num]}")
  await ctx.send(links[entry])

@bot.command()
async def sus(ctx):
  await ctx.send(str(ctx.author.mention)+ " is sus.")

@bot.command()
async def vent(ctx):
  await ctx.send(str(ctx.author.mention)+" vented!")

@bot.command()
async def isRed(ctx):
  if(str(ctx.message.author)=="redguy999#1564"):
    await ctx.send("You are Redguy")
  else:
    await ctx.send("You are not Redguy")

@bot.command()
async def rickRoll(ctx,member:nextcord.Member):
  await ctx.send(str(member.mention) +" https://www.youtube.com/watch?v=dQw4w9WgXcQ")

@bot.command()
async def uploadFile(ctx):
  if(not os.path.isdir("vault")):
    os.mkdir("vault")
  for file in ctx.message.attachments:
    try:
      file_url = file.url
      r = requests.get(file_url, stream = True)
      fileName=re.findall("[0-9]+/[0-9]+/(.+)$",file_url)[0]
      with open("vault/"+fileName,"wb") as incoming:#downloads the file,and places it in the current directory.
      #The name of the dmg file just needs to be kept a constant, we're gonna delete it anyway.
        for chunk in r.iter_content(chunk_size=1024*1024):
          # writing one chunk at a time to the file
          if chunk:
              incoming.write(chunk)
      incoming.close()
    except:
      await ctx.send("An error accorded when trying to download: "+file.url+" skipping...")
  await ctx.send("Files sent.")
  