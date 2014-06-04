from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector, Selector
from qrator.items import CraigslistSampleItem, QratorItem
import os
import json
import time

# API's
# http://developer.nytimes.com/docs
# http://developer.usatoday.com/

# def parse(self, response):
#     # Beautiful soup related parse(), if ever needed..
#     hxs = Selector(response)
#     #headers = hxs.xpath("//item").extract()
#     #headers = hxs.xpath("//category").extract()
#     headers = hxs.xpath("//item").extract()
#     # print type(headers[0])
#     items = []
#     for header in headers:
#         soup = Soup(header, features="xml")
#         entries = soup.findAll('item')
#         for entry in entries:
#             print entry.find('category')
#             items.append(entry.find('title'))
#             # print header.xpath('title').extract()
#         # items.append(header)
#     print items[0]
#     # return items

class MySpider(BaseSpider):
    
    '''
    Crags List.
    '''
    name = "craig"
    allowed_domains = ["craigslist.org"]
    start_urls = ["http://sfbay.craigslist.org/npo/"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select("//span[@class='pl']")
        items = []
        for titles in titles:
            item = CraigslistSampleItem()
            item["title"] = titles.select("a/text()").extract()
            item["link"] = titles.select("a/@href").extract()
            items.append(item)
        return items

class MitTechSpider(BaseSpider):

    '''
    MIT "The Tech".
    '''
    name = "mitTheTech"
    allowed_domains = ["tech.mit.edu"]
    start_urls = ["http://tech.mit.edu/rss/"]

    def parse(self, response):
        sel = Selector(response)
        headers = sel.xpath('//tr')
        items = {}
        for header in headers:
            temp_title = str(header.xpath("td/text()").extract()[0])
            items[temp_title] = []
            for entry in header.xpath('//td'):
                item2 = {}
                try:
                    item2['link'] = str(entry.xpath("a/@href").extract()[0])
                    item2['text'] = str(entry.xpath("a/text()").extract()[1])
                    item2['type'] = temp_title
                    items[temp_title].append(item2)
                except:
                    continue
                # print item2
        for key, value in items.iteritems():
            print "\nType: %s\nContent: %s\n" % (key, value)
        # return items


class NYHomeSpider(BaseSpider):

    '''
    New York Times Home. 
    '''
    name = "nytHome"
    allowed_domains = ["nytimes.com"]
    start_urls = ["http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"]

    def parse(self, response):
        sel = Selector(response)
        headers = sel.xpath("//item")
        items = []
        for header in headers:
            item = {}
            item["title"] = header.xpath('title/text()').extract()
            item["link"] = header.xpath('link/text()').extract()
            item['description'] = header.xpath('description/text()').extract()
            item['category'] = header.xpath('category/text()').extract()
            item['pubDate'] = header.xpath('pubDate/text()').extract()
            items.append(item)
            print item
        if os.path.exists('data'):
            pass
        else:
            os.mkdir('data')
        f = open('data/' +
                 time.strftime("NYHome-%Y-%m-%d-%H-NYHome") +
                 '.json', 'wb')
        f.write(json.dumps(items))
        f.close()


class NYInternationalHomeSpider(BaseSpider):

    '''
    New York Times Internation-Home.
    '''
    name = "nytInternationalHome"
    allowed_domains = ["nytimes.com"]
    start_urls = [
        "http://rss.nytimes.com/services/xml/rss/nyt/InternationalHome.xml"]

    def parse(self, response):
        sel = Selector(response)
        headers = sel.xpath("//item")
        items = []
        for header in headers:
            item = {}
            item["title"] = header.xpath('title/text()').extract()
            item["link"] = header.xpath('link/text()').extract()
            item['description'] = header.xpath('description/text()').extract()
            item['category'] = header.xpath('category/text()').extract()
            item['pubDate'] = header.xpath('pubDate/text()').extract()
            items.append(item)
            print item
        if os.path.exists('data'):
            pass
        else:
            os.mkdir('data')
        f = open('data/' +
                 time.strftime("NYInternationalHome-%Y-%m-%d-%H-NYInternationalHome") +
                 '.json', 'wb')
        f.write(json.dumps(items))
        f.close()

class HBRSpider(BaseSpider):

    '''
    Harvard Business Review. 
    '''
    name = "HBR"
    allowed_domains = ["harvardbusiness.org"]
    start_urls = ["http://feeds.harvardbusiness.org/harvardbusiness"]

    def parse(self, response):
        sel = Selector(response)
        # print sel
        regularItems = sel.xpath("//title").extract() #[@class='regularitem']
        print regularItems
        # items = []
        # for titles in titles:
        #     item = CraigslistSampleItem()
        #     item["title"] = titles.select("a/text()").extract()
        #     item["link"] = titles.select("a/@href").extract()
        #     items.append(item)

        # sel = Selector(response)
        # headers = sel.xpath("//item")
        # items = []
        # for header in headers:
        #     item = {}
        #     item["title"] = header.xpath('title/text()').extract()
        #     item["link"] = header.xpath('link/text()').extract()
        #     item['description'] = header.xpath('description/text()').extract()
        #     item['category'] = header.xpath('category/text()').extract()
        #     item['pubDate'] = header.xpath('pubDate/text()').extract()
        #     items.append(item)
        #     print item
        # if os.path.exists('data'):
        #     pass
        # else:
        #     os.mkdir('data')
        # f = open('data/' +
        #          time.strftime("NYHome-%Y-%m-%d-%H-NYHome") +
        #          '.json', 'wb')
        # f.write(json.dumps(items))
        # f.close()


class FTSpider(BaseSpider):

    '''
    Financial Times.
    '''
    name = "fTimes"
    allowed_domains = ["ft.com"]
    start_urls = ["http://www.ft.com/rss"]
    def parse(self, response):
        pass


class HNSpider(BaseSpider):

    '''
    Hacker News.
    '''
    name = "hackerNews"
    allowed_domains = ["ycombinator.com"]
    start_urls = ["https://news.ycombinator.com/rss"]
    def parse(self, response):
        pass


class MitTechReviewSpider(BaseSpider):

    '''
    MIT Tech Review.
    '''
    name = "techReview"
    allowed_domains = ["technologyreview.com"]
    start_urls = ["http://www.technologyreview.com/connect/#rss"]
    def parse(self, response):
        pass


class BusinessInsiderSpider(BaseSpider):

    '''
    Business Insider.
    '''
    name = "bInsider"
    allowed_domains = ["businessinsider.com"]
    start_urls = ["http://www.businessinsider.in/rss_feeds.cms"]
    def parse(self, response):
        pass


class USATodaySpider(BaseSpider):

    '''
    USA Today.
    '''
    name = "usaToday"
    allowed_domains = ["usatoday.com"]
    start_urls = ["http://content.usatoday.com/marketing/rss/index.aspx"]
    def parse(self, response):
        pass


class LATimesSpider(BaseSpider):

    '''
    LA Times.
    '''
    name = "laTimes"
    allowed_domains = ["latimes.com"]
    start_urls = ["http://www.latimes.com/la-los-angeles-times-rss-feeds-20140507-htmlstory.html"]
    def parse(self, response):
        pass


class TheTimesSpider(BaseSpider):

    '''
    The Times.
    '''
    name = "theTimes"
    allowed_domains = ["thetimes.co.uk"]
    start_urls = ["http://www.thetimes.co.uk/tto/feedindex/"]
    def parse(self, response):
        pass


class WSJSpider(BaseSpider):

    '''
    WallStreet Journal.
    '''
    name = "wsj"
    allowed_domains = ["wsj.com"]
    start_urls = ["http://online.wsj.com/public/page/rss_news_and_feeds.html"]
    def parse(self, response):
        pass


class DiscoverMagSpider(BaseSpider):

    '''
    Discover Magazine.
    '''
    name = "discoverMag"
    allowed_domains = ["discovermagazine.com"]
    start_urls = ["http://discovermagazine.com/rss"]
    def parse(self, response):
        pass


class ArsTechnicaSpider(BaseSpider):

    '''
    Ars Technica.
    '''
    name = "arsTechnica"
    allowed_domains = ["arstechnica.com"]
    start_urls = ["arstechnica.com/rss-feeds/"]
    def parse(self, response):
        pass


# class Spider(BaseSpider):

#     '''
#     New York Times Internation-Home.
#     '''
#     name = "HBR"
#     allowed_domains = ["harvardbusiness.org"]
#     start_urls = ["http://feeds.harvardbusiness.org/harvardbusiness"]
#     def parse(self, response):
#         pass
