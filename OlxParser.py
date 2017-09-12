# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import requests
import json
from bs4 import BeautifulSoup


def parser():
    triger = False
    def trade_spider(max_pages, url, tag, classCss,):
        page = 0
        while page <= max_pages:
            source_code = requests.get(url)
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text, "html.parser")
            allLinks = soup.findAll(tag, {'class': classCss})
            headers = []
            for link in allLinks:
                headers.append({'text': link.strong.string, 'link': link.a['href']})
           #page += 1
            return headers



    url = 'https://www.olx.pl/praca/informatyka/warszawa/?search%5Bdistrict_id%5D=351&search%5Bfilter_enum_type%5D%5B0%5D=practice'
    headersInterships = trade_spider(0, url, 'h3', 'x-large lheight20 margintop5')

    url = 'https://www.olx.pl/praca/informatyka/warszawa/q-javascript/'
    headersJavascript = trade_spider(0, url, 'tr', 'wrap')

    with open('parser.json') as readJson:
        dataJson = json.load(readJson)

    headers = headersInterships + headersJavascript
    newHeaders = []

    for i in range(len(headers)):
        if dataJson[i]['text'] != headers[i]['text']:
            newHeaders.append(headers[i])
            triger = True

    if triger == True:
        print (newHeaders)
        with open('parser.json', 'w') as file:
                json.dump(headersInterships + headersJavascript, file, indent=2, ensure_ascii=False)
        return newHeaders
