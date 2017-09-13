# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import requests
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
