import requests
import sys
import bs4
import webbrowser

res = requests.get('https://google.com/search?q='+''.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text,"html.parser")

# linkElements is going to be a variable which take help of beautiful soup to link html parser
linkElements = soup.select('.r a')
linksToOpen = min(5,len(linkElements))
for i in range(linksToOpen):
    webbrowser.open_new_tab('https://google.com'+linkElements[i].get('href'))