"""
@author: gpwolfe

Settings in tutorial/tutorial/settings.py includes options for activating
the auto-tuning of requests sent, causing spider to wait for longer before
accessing website again, preventing 429 errors.

"""
import scrapy


class ZnsSpider(scrapy.Spider):
    name = "zns_text"
    allowed_domains = ['znsbahamas.com']
    

    def start_requests(self):
        urls = [
            'https://znsbahamas.com/c-w-saunders-students-temporarily-move-to-ub-campus/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        text = {'text': ' '.join(response.css('article p::text').getall())}
        yield text

        next_page_url = response.xpath(
            """//div[contains(@class, "td-block-span6 td-post-next-post")
             and contains(
                 .//span, "Next article")]/div/a/@href""").extract_first()
        if next_page_url:
            yield scrapy.Request(next_page_url, callback=self.parse)