import requests
import bs4

result = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")

soup = bs4.BeautifulSoup(result.text, "lxml")

content_table_elems = soup.select('.vector-toc-text span:nth-child(2)')

for elem in content_table_elems:
    elem_text = elem.getText()

    print(elem_text)