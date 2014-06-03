from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector, Selector
from qrator.items import CraigslistSampleItem, QratorItem

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
      ##headers = hxs.select("//h3[@class='header']")
      #headers = hxs.xpath("//item").extract()
      headers = hxs.xpath("//category").extract()
      print headers
      items = []
      '''
      for header in headers:
        item ["title"] = header.select("a/text()").extract()
        item ["link"] = header.select("a/@href").extract()
        items.append(item)
        return items
      '''
