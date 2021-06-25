import scrapy
class QuotesSpider(scrapy.Spider):
    name = "toscrapecss"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for toscrapecss in response.css('div.quote'):
            yield {
                'text': toscrapecss.css('span.text::text').get(),
                'author': toscrapecss.css('small.author::text').get(),
                'tags': toscrapecss.css('div.tags a.tag::text').getall(),
            }