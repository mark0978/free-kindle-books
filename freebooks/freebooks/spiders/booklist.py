# -*- coding: utf-8 -*-
import scrapy
import decimal

ZERO = decimal.Decimal('0.0')

class BooklistSpider(scrapy.Spider):
    name = 'booklist'
    allowed_domains = ['amazon.com']
    start_urls = [
        'https://www.amazon.com/s?k=free+kindle+books&rh=n%3A283155%2Cn%3A16272&dc&qid=1548021972&rnid=2941120011&ref=sr_nr_n_15'
    ]

    def parse(self, response):
        
        for e in response.css('div.s-item-container'):
            self.log("Fetched %s" % response.url)
            title = e.css('h2::text').extract_first()
            if title:
                price = decimal.Decimal(e.css('span.sx-price-whole::text').extract_first() 
                                        + '.' 
                                        + e.css('sup.sx-price-fractional::text').extract_first())
                if price == ZERO:
                    yield {
                        'title': title,
                        'author': e.css('span.a-size-small > a.a-link-normal::text').extract_first(),
                        'price': price,
                        'purchase-href': response.urljoin(e.css('a.a-link-normal::attr(href)').extract_first()),
                    }
            next_url = response.css('a#pagnNextLink::attr(href)').extract_first()
            if next_url:
                yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse)
