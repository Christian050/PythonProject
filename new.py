import bs4
import requests

res=requests.get("https://ghana.gov.gh/home")
print("The object type: ", type(res))

soup=bs4.BeautifulSoup(re.text, "html5lib")
print("The object type: ", type(soup))
soup.select(".mw-headline")
for i in soup.select("mw-headline"):
    print(i.text, end=",")
# change link