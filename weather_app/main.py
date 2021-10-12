import requests
import bs4

search = "weather in kollam"
url = f"https://www.google.com/search?&q={search}"

r = requests.get(url)

s = bs4.BeautifulSoup(r.text, "html.parser")
update = s.find("div", class_="BNeawe").text
print(update)
#you have to install 2 packages
# 1 - bs4 --> pip install bs4
# 2 - requests --> pip install requestes