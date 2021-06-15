"""
@author: gpwolfe

Scrape news article text from ZNS Bahamas news website (znsbahamas.com)

Usage from command line:
From project's top-level directory
>>> python3 zns_scrapy_text.py

Edit "self.count < [number]" in line 48 to limit number of articles scraped.

"""
from scrapy import Field, Item, Request, Spider
from scrapy.crawler import CrawlerProcess

class ZnsItem(Item):
    text = Field()


class ZnsSpider(Spider):
    name = "zns_text"
    allowed_domains = ['znsbahamas.com']
    custom_settings = {
        'AUTOTHROTTLE_ENABLED': True,
        'AUTOTHROTTLE_START_DELAY': 1,
        'AUTOTHROTTLE_MAX_DELAY': 60,
        'AUTOTHROTTLE_TARGET_CONCURRENCY': 1.0,
        }
    # count = 0

    def start_requests(self):
        urls = [
            # 'https://znsbahamas.com/police-investigating-the-countrys-latest-homicide-3/'
            'https://znsbahamas.com/covid-19-update-26-3-2021/',
        ]
        for url in urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        item = ZnsItem()
        item['text'] = ' '.join(response.css('article p::text').getall())
        # if len(item['text']) > 0:
            # self.count += 1
        yield item

        prev_page_url = response.xpath(
            """//div[contains(@class, "td-block-span6 td-post-prev-post")
             ]/div/a/@href""").extract_first()
        if prev_page_url:
            yield Request(prev_page_url, callback=self.parse)


def run_spider():
    process = CrawlerProcess(settings={
        'FEEDS': {
            'articles_100K_nolim.csv': {'format': 'csv'},
            },
        })
    process.crawl(ZnsSpider)
    process.start()


if __name__ == '__main__':
    run_spider()
