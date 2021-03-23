import scrapy
class ExtractUrls(scrapy.Spider):
   name = "fetch"
   # generator Function
   def start_requests(self):
      # enter the URL
      urls = ['https://www.houseofindya.com/zyra/necklace/cat', ]
      for url in urls:
         yield scrapy.Request(url = url, callback = self.parse)
   # Parse function
   def parse(self, response):
      title = response.css('title::jewelry').extract_first()
      # Get anchor tags
      links = response.css('a::attr(href)').extract()
      for link in links:
         yield {
            'title': jewelry,
            'links': link
         }
         if 'tutorialspoint' in link:
            yield scrapy.Request(url = link, callback = self.parse)
from urllib.request import urlopen
my_html = urlopen("https://www.houseofindya.com/zyra/necklace/cat")
print(my_html.read())
