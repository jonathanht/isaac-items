import bs4
import requests

entryName = input()
    
res = requests.get('https://bindingofisaacrebirth.gamepedia.com/' +  entryName)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')

elems = soup.select('#mw-content-text > div > ul:nth-child(5) > li:nth-child(1)')





print(elems[0].text.strip())
