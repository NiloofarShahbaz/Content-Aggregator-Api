import scrapy
from ..items import RealPythonItem


class RealPythonCrawler(scrapy.Spider):
    name = 'realpython_crawler'
    allowed_domains = ['realpython.com']
    start_urls = [
        'https://realpython.com/'
    ]

    def parse(self, response):
        posts = response.xpath(
            '//div[contains(@class, "col-12")]/div[@class="card border-0"]/div[contains(@class, "card-body")]'
        )
        for post in posts:
            item = RealPythonItem()
            item['url'] = post.xpath('a/@href').extract()[0]
            item['title'] = post.xpath('a/h2/text()').extract()[0]
            item['tags'] = post.xpath('p[@class="card-text"]/small/a[contains(@class, "badge")]/text()').extract()
            yield item
