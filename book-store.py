import re
import requests
from bs4 import BeautifulSoup

url_base = "http://books.toscrape.com/"


def in_stock(title, topic) -> bool:
    soup = get_and_parse_url(url_base)
    menu = soup.find_all("ul", {"class": "nav nav-list"})

    url_topic = get_url_from_topic(topic, menu[0])
    if not url_topic:
        return False

    url_topic = url_topic.replace("index.html", "")
    all_books = get_all_books(url_topic)
    for book in all_books:
        if book["title"].lower() == title.lower():
            return True
    return False


def get_and_parse_url(url: str):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    return (soup)


def get_url_from_topic(topic: str, menu) -> str:
    for item in menu.find_all("li"):
        if item.a.text.strip().lower() == topic.lower():
            return f"{url_base}{item.a['href']}"
    return ""


def get_all_books(url_find: str) -> list:
    list_return = []
    soup = get_and_parse_url(url_find)
    pages_count = get_pages(soup.text)

    if pages_count == 0:
        return extract_books_from_catalog(f"{url_find}/index.html")

    for page_num in range(0, pages_count + 1):
        books = extract_books_from_catalog(f"{url_find}page-{page_num}.html")
        list_return.extend(books)

    return list_return


def extract_books_from_catalog(url: str) -> list:
    list_return = []
    soup = get_and_parse_url(url)
    books = soup.find_all("li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})

    for book in books:
        title = book.findAll("h3")
        list_return.append(
            {
                "title": title[0].find("a")["title"].strip(),
            }
        )

    return list_return


def get_pages(content) -> int:
    pattern = "Page [0-9]+ of ([0-9]+)"
    matcher = re.search(pattern, content)
    if not matcher:
        return 0
    pages = int(matcher.group(1))
    return pages


if __name__ == "__main__":
    print(in_stock(title="While You Were Mine", topic="Historical Fiction"))
