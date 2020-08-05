import scrapy


class BestsellersSpider(scrapy.Spider):
    name = 'bestsellers'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['http://www.glassesshop.com/bestsellers/']

    def parse(self, response):
        for glass in response.xpath("//div[@id='product-lists']/div"):
            if glass.xpath(".//a[@href='/buy-one-get-one-free']"):
                continue
            yield {
                'url': glass.xpath(".//div[@class='product-img-outer']/a/@href").get(),
                'img_url': glass.xpath(".//div[@class='product-img-outer']/a/img/@src").get(),
                'name': glass.xpath(".//div[@class='p-title']/a/@title").get(),
                'price': glass.xpath(".//div[@class='p-price']//span/text()").get()
            }

        next_page = response.xpath("//ul[@class='pagination']/li[position() = last()]/a/@href").get()

        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
