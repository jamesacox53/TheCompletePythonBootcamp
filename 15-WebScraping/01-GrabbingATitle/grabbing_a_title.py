import requests
import bs4

result = requests.get("http://www.example.com")

soup = bs4.BeautifulSoup(result.text, "lxml")

title_elem = soup.select('title')[0]

print(title_elem.getText())