# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SalonItem(scrapy.Item):
    # define the fields for your item here like:
    サロン名 = scrapy.Field()
    電話番号 = scrapy.Field()
    住所 = scrapy.Field()
    緯度 = scrapy.Field()
    経度 = scrapy.Field()
    営業時間 = scrapy.Field()
    定休日 = scrapy.Field()
    サロンホームページ = scrapy.Field()
    カット価格 = scrapy.Field()
    席数 = scrapy.Field()
    スタッフ数 = scrapy.Field()
    ホットペッパーページ = scrapy.Field()
    ホットペッパー求人ページ = scrapy.Field()
