import random
import sys 
import requests
from discord_webhook import DiscordWebhook
from bs4 import BeautifulSoup


num = random.randint(0,100000)
nnum = (num < 100000)
url = 'https://flipbook.apps.gwo.pl/display/{}'  .format(random.randint(0,60000))


reqs = requests.get(url)
  


soup = BeautifulSoup(reqs.text, 'html.parser')
  
gwo = "Gdańskie Wydawnictwo Oświatowe"

for title in soup.find_all('title'):
    webhk = title.get_text()
    print(title)
    if gwo in webhk:
        quit()
    stdoutOrigin=sys.stdout
    webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/903722178678239233/CaJj2UuGrdOQwq23I1BKYDTivM48iu8955LnIThITzA1sYABFDnekbMXyIJv2r7pkF48', content = webhk + "\n" + "> " + url)
    response = webhook.execute()



