# Our goal is to get the title of every book with a 2 star rating
import requests
import bs4
import os

def get_url(page_num):
    return "http://books.toscrape.com/catalogue/page-" + str(page_num) + ".html"

result = requests.get(get_url(page_num=1))

soup = bs4.BeautifulSoup(result.text, "lxml")

elems = soup.select('.product_pod')

print(len(elems))