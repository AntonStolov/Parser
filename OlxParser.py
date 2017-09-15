# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import requests
import json
from bs4 import BeautifulSoup
import pracuj


def parser():
    triger = False
    def trade_spider(max_pages, url, tag, class_css, ):
        page = 0
        while page <= max_pages:
            source_code = requests.get(url)
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text, "html.parser")
            allLinks = soup.findAll(tag, {'class': class_css})
            headers = []
            for link in allLinks:
                headers.append({'text': link.strong.string, 'link': link.a['href']})
           #page += 1
            return headers



    url = 'https://www.olx.pl/praca/informatyka/warszawa/?search%5Bdistrict_id%5D=351&search%5Bfilter_enum_type%5D%5B0%5D=practice'
    headers_interships = trade_spider(0, url, 'h3', 'x-large lheight20 margintop5')

    url = 'https://www.olx.pl/praca/informatyka/warszawa/q-javascript/'
    headers_javascript = trade_spider(0, url, 'tr', 'wrap')

    url = 'https://www.pracuj.pl/praca/JavaScript%20junior;kw/warszawa;wp/it%20-%20rozw%c3%b3j%20oprogramowania;cc,5016'
    headers_pracuj = pracuj.trade_pracuj_pl(0, url, 'h2', 'o-list_item_link')

    url = 'https://www.pracuj.pl/praca/front%20end%20junior;kw/warszawa;wp/it%20-%20rozw%c3%b3j%20oprogramowania;cc,5016'
    headers_pracuj_front = pracuj.trade_pracuj_pl(0, url, 'h2', 'o-list_item_link')

    with open('parser.json') as readJson:
        data_json = json.load(readJson)

    headers = headers_interships + headers_javascript + headers_pracuj + headers_pracuj_front
    new_headers = []

    count = 0
    for i in range(len(headers)):
        not_found = True

        for j in range(len(data_json)):
            if  headers[i]['text'] == data_json[j]['text']:
                not_found = False

        if not_found == True:
            new_headers.append(headers[i])
            triger = True

    if triger == True:
        print (new_headers)
        with open('parser.json', 'w') as file:
                json.dump(headers, file, indent=2, ensure_ascii=False)

        return new_headers
