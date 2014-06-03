from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector, Selector
from qrator.items import CraigslistSampleItem, QratorItem

from bs4 import BeautifulSoup as Soup

class MySpider(BaseSpider):
  name = "craig"
  allowed_domains = ["craigslist.org"]
  start_urls = ["http://sfbay.craigslist.org/npo/"]

  def parse(self, response):
      hxs = HtmlXPathSelector(response)
      titles = hxs.select("//span[@class='pl']")
      items = []
      for titles in titles:
          item = CraigslistSampleItem()
          item ["title"] = titles.select("a/text()").extract()
          item ["link"] = titles.select("a/@href").extract()
          items.append(item)
      return items
      
class MitSpider(BaseSpider):
  name = "techReview"
  allowed_domains = ["tech.mit.edu"]
  start_urls = ["http://tech.mit.edu/rss/"]
  
  def parse(self, response):
    hxs = HtmlXPathSelector(response)
    titles = hxs.select('//table')
    items = []
    for title in titles:
      item = QratorItem()
      item ["title"] = titles.select("a/text()").extract()
      item ["link"] = titles.select("@/href").extract()
      items.append(item)
      print title, link
    return items
    
## ny home + ny international home
class NYSpider(BaseSpider):
  name = "nytHome"
  allowed_domains = ["nytimes.com"]
  start_urls = ["http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"]

  def parse(self, response):
      hxs = Selector(response)
      #headers = hxs.xpath("//item").extract()
      #headers = hxs.xpath("//category").extract()
      headers = hxs.xpath("//item").extract()
      #print type(headers[0])
      items = []
      for header in headers:        
        soup = Soup(header, features="xml")
        entries = soup.findAll('item')
        for entry in entries:
          print entry.find('category').string
        #print header.xpath('title').extract()
        #items.append(header)
      #return items
      
