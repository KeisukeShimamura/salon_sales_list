import scrapy
from bs4 import BeautifulSoup
from scraping.items import SalonItem
import json
import datetime

class HotPapperBeautySpider(scrapy.Spider):
    name = 'hot_papper_beauty'
    allowed_domains = ['beauty.hotpepper.jp']
    start_urls = [
        'https://beauty.hotpepper.jp/pre01/',
    ]

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        
        salon_h3_list = soup.find_all("h3", class_="slnName")
        for salon_h3 in salon_h3_list:
            link = salon_h3.find('a')
            # サロンページへ遷移
            yield scrapy.Request(link.get('href'), self.parse_salon_page)

        # 次ページへ移動
        next_link = soup.find("li", class_="afterPage").findNext('a')
        yield scrapy.Request(next_link.get('href'), callback=self.parse)

    def parse_salon_page(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')

        item = SalonItem()
        item['サロン名'] = soup.h1.get_text()
        item['ホットペッパーページ'] = response.url
        for th in soup.find('table', class_='slnDataTbl').find_all('th'):
            if th.get_text() == '住所':
                item["住所"] = th.next_element.findNext('td').get_text().strip()
            elif th.get_text() == '営業時間':
                item["営業時間"] = th.next_element.findNext('td').get_text().strip()
            elif th.get_text() == '定休日':
                item["定休日"] = th.next_element.findNext('td').get_text().strip()
            elif th.get_text() == 'お店のホームページ':
                item["サロンホームページ"] = th.next_element.findNext('td').get_text().strip()
            elif th.get_text() == 'カット価格':
                item["カット価格"] = th.next_element.findNext('td').get_text().strip()
            elif th.get_text() == '席数':
                item["席数"] = th.next_element.findNext('td').get_text().strip()
            elif th.get_text() == 'スタッフ数':
                item["スタッフ数"] = th.next_element.findNext('td').get_text().strip()
            elif th.get_text() == 'スタッフ募集':
                item["ホットペッパー求人ページ"] = th.next_element.findNext('td').findNext('a').get('href')

        for script in soup.find_all('script', attrs={'type': 'application/ld+json'}):
            data = json.loads(script.get_text())
            if ('@type' not in data):
                continue
            if (data['@type'] != 'BeautySalon'):
                continue
            if ('telephone' in data):
                item['電話番号'] = data['telephone']

        item['ホットペッパー掲載確認日'] = datetime.date.today()
    
        yield item
