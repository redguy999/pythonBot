#Azat will edit this
from urllib.request import urlopen
from bs4 import BeautifulSoup
  
htmldata = urlopen('https://www.google.com/search?q=cats&rlz=1C5GCEM_enUS980US980&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi6m6CA0-T3AhWrkIkEHQzRDYgQ_AUoAXoECAIQAw&biw=1440&bih=789&dpr=1')
soup = BeautifulSoup(htmldata, 'html.parser')
images = soup.find_all('img')
  
for item in images:
    print(item['src'])
