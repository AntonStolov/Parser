# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import requests
import json
from bs4 import BeautifulSoup


def trade_pracuj_pl(max_pages, url, tag, classCss, ):
    page = 0
    while page <= max_pages:
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        allLinks = soup.findAll(tag, {'class': classCss})
        headers = []
        for link in allLinks:
            headers.append({'text': link.a.string, 'link': 'https://www.pracuj.pl' + link.a['href']})
            # page += 1
        return headers


# url = 'https://www.pracuj.pl/praca/JavaScript%20junior;kw/warszawa;wp/it%20-%20rozw%c3%b3j%20oprogramowania;cc,5016'
# headersPracuj = trade_spider(0, url, 'h2', 'o-list_item_link')