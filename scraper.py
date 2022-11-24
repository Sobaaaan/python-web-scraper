from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

url_to_scrape = "https://planetdesert.com/collections/cactus"

request_page = urlopen(url_to_scrape)
page_html = request_page.read()
request_page.close()

html_soup = BeautifulSoup(page_html, 'html.parser')

cactus_items = html_soup.find_all(
    'span', class_="snize-overhidden")

filename = 'product.csv'
f = open(filename, 'w')

headers = 'Title, Price \n'

f.write(headers)

for cactus in cactus_items:
    title = cactus.find('span', class_="snize-title").text
    price = cactus.find('span', class_="snize-price  money ").text

    f.write(title + ',' + price)

f.close()
