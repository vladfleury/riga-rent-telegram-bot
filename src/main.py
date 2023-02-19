import bs4
from bs4 import BeautifulSoup
import requests
import csv

source = requests.get("https://www.ss.lv/lv/real-estate/flats/riga/centre/").text
soup = BeautifulSoup(source, 'html.parser')

csv_file = open('cms_appartment_scrape.csv', 'w')
csv_write = csv.writer(csv_file)
csv_write.writerow(['Address', 'Price', 'Area', 'Link'])

# Parsing the right table.
table = soup.find('table', {'align': 'center', 'cellpadding': '2', 'border': '0', 'width': '100%'})

price = []
area = []
link = []
address = []

# Getting every element from website.
for tr_element in table.find_all('tr'):
    try:
        td_element = tr_element.find_all('td')[3].text
        td_element_price = tr_element.find_all('td')[9].text
        td_element_area = tr_element.find_all('td')[5].text
        td_element_link = tr_element.find('a')['href']
    except Exception as e:
        td_element = None
        td_element_price = None
        td_element_area = None
        td_element_link = None
    address.append(td_element)
    price.append(td_element_price)
    area.append(td_element_area)
    link.append(td_element_link)

# Dropping header and footer of a list.
address.pop(0)
address.pop(-1)
price.pop(0)
price.pop(-1)
area.pop(0)
area.pop(-1)
link.pop(0)
link.pop(-1)

# adding ss.lv to a link, because the link wasn't full
prefix = 'ss.lv'
link_full = [prefix + x for x in link]

# Combine the lists into a list of tuples before writing into a CSV
data = zip(address, price, area, link_full)

for row in data:
    csv_write.writerow(row)

csv_file.close()