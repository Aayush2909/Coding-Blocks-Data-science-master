#Pre-requisites: Scrapy (Web scraping Framework)
#Create a new project using: scrapy startproject  <projectname>
#Goto <projectname>/<projectname>/spiders and create your own spider(python file) for crawling web

#Code for the spider-

import scrapy

class BooksSpider(scrapy.Spider):
    name = "books"

    def start_requests(self):
        urls = [
            'http://books.toscrape.com/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        with open("result.csv", "a+") as f:
            books = response.css("li.col-xs-6")
            for b in books:
                info = []
                img = b.css("div.image_container a img::attr(src)").get()
                info.append(img)
                title = b.css("h3")[0].css("a::attr(title)").get()
                if ',' in title:
                    title = '"'+title+'"'
                info.append(title)
                price = b.css("div.product_price p.price_color::text").get()
                info.append('Â'+price)

                data = ','.join(info)
                f.write(data)
                f.write('\n')

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            url = response.urljoin(next_page)
            yield scrapy.Request(url=url, callback=self.parse)


#Run the spider: scrapy crawl books
#Here, "books" is the name of the spider set in the code


            
