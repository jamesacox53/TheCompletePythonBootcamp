# Our goal is to get the title of every book with a 2 star rating
import requests
import bs4

def get_two_star_book_titles():
    two_star_book_titles = []
    
    for page_num in range(1, 51):
        two_star_titles = get_two_star_titles(page_num)

        two_star_book_titles.extend(two_star_titles)

    return two_star_book_titles

def get_two_star_titles(page_num):
    page_url = get_url(page_num)

    books = get_books(page_url)
    two_star_books = get_two_star_books(books)

    two_star_titles = get_titles(two_star_books)
    return two_star_titles

def get_url(page_num):
    return "http://books.toscrape.com/catalogue/page-" + str(page_num) + ".html"

def get_books(page_url):
    result = requests.get(page_url)
    soup = bs4.BeautifulSoup(result.text, "lxml")

    books = soup.select('.product_pod')

    return books

def get_two_star_books(books):
    two_star_books = []

    for book in books:
        two_star_elems = book.select('.star-rating.Two')

        if len(two_star_elems) > 0:
            two_star_books.append(book)

    return two_star_books
         
def get_titles(books):
    titles = []

    for book in books:
        title_elem = book.select('h3 > a')[0]
        title_attr = title_elem['title']

        title = str(title_attr)

        titles.append(title)

    return titles

if __name__ == '__main__':
    two_star_book_titles = get_two_star_book_titles()
    print(two_star_book_titles)
    print(len(two_star_book_titles))