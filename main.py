import requests
import lxml
import bs4
from bs4 import BeautifulSoup
import csv


source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'html.parser')

csv_file = open('cms_scrape.csv', 'w')
csv_write = csv.writer(csv_file)
csv_write.writerow(['headline', 'summary', 'videolink'])

for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)


    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']
        vid_id = vid_src.split('/')[4]
        vid_id = vid_src.split('?')[0]
        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None

    print(yt_link)

    print()
    csv_write.writerow([headline, summary, yt_link])

csv_file.close()