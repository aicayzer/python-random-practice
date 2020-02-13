import scrapy
class CompanySpider(scrapy.Spider):
    name = "companyspider"
    start_urls = ["https://picapital.co.uk/past-events/"]

    def parse(self, response):
            yield {
            "title": article.css("header#upcoming-events")
            }





            # next = response.css(".next > a::attr(href)").extract_first()
            # if next:
            #     yield response.follow(next, self.parse)
