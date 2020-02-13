import scrapy
class CompanySpider(scrapy.Spider):
    name = "companyspider"
    start_urls = ["https://www.angel.co/companies/"]

    def parse(self, response):
        for article in response.css("base startup"):
            yield {
            "name": article.css(".startup-link")
            }





            # next = response.css(".next > a::attr(href)").extract_first()
            # if next:
            #     yield response.follow(next, self.parse)
