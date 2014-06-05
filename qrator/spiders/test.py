from scrapy.spider import BaseSpider
import scrapy.http
from scrapy.selector import HtmlXPathSelector, Selector
from qrator.items import CraigslistSampleItem, QratorItem
import os
import re
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
        print items[0]
        if os.path.exists('data'):
            pass
        else:
            os.mkdir('data')
        f = open('data/' +
                 time.strftime("NYHome-%Y-%m-%d-%H-%M-%S-NYHome") +
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
        print items[0]
        if os.path.exists('data'):
            pass
        else:
            os.mkdir('data')
        f = open('data/' +
                 time.strftime("NYInternationalHome-%Y-%m-%d-%H-%M-%S-NYInternationalHome") +
                 '.json', 'wb')
        f.write(json.dumps(items))
        f.close()

class FinancialTimeSpider(BaseSpider):

    '''
    Financial Times All.
    '''
    name = "ft"
    allowed_domains = ["ft.com"]
    start_urls = ["http://www.ft.com/rss"]

    def parse(self, response):        
        sel = Selector(response)
        rssItems = [x.xpath('text()').extract() + x.xpath('@href').extract() \
                    for x in sel.xpath("//a") if x.xpath('@href').extract()[0].find('/rss/')!=-1]
        for item in rssItems:
            print item[1]
            selItem = Selector(scrapy.http.XmlResponse(item[1]))
            print selItem.extract()
            # print selItem.extract()
            # xmlItems = selItem.xpath("//title")
            # print xmlItems.extract()
        # for rss in rssItems:
            # print rss.xpath('href').extract()

class HBRSpider(BaseSpider):

    '''
    Harvard Business Review. (with HtmlXPathSelector)
    '''
    name = "HBR"
    allowed_domains = ["harvardbusiness.org"]
    start_urls = ["http://feeds.harvardbusiness.org/harvardbusiness"]

    def parse(self, response):
        sel = HtmlXPathSelector(response)
        entries = sel.xpath('//entry')
        items = []
        for entry in entries:
            item = {}
            item['title'] = entry.xpath('title/text()').extract()[0]
            item['id'] = entry.xpath('id/text()').extract()[0]
            item['link'] = entry.xpath('link/@href').extract()[0]
            item['updated'] = entry.xpath('updated/text()').extract()[0]
            item['summary'] = entry.xpath('summary/text()').extract()
            # temp = entry.select('//author')
            item['author'] = {}
            item['author']['name'] = entry.xpath('author/name/text()').extract()
            item['author']['uri'] = entry.xpath('author/uri/text()').extract()
            #temp = entry.select('//contributor')
            item['contributor'] = {}
            item['contributor']['name'] = entry.xpath('contributor/name/text()').extract()
            item['contributor']['uri'] = entry.xpath('contributor/uri/text()').extract()
            item['category'] = entry.xpath('category/@term').extract()
            item['content'] = entry.xpath('content/text()').extract()[0]
            item['origlink'] = entry.xpath('origlink/text()').extract()[0]
            items.append(item)
        print items[0]
        if os.path.exists('data'):
            pass
        else:
            os.mkdir('data')
        f = open('data/' +
                 time.strftime("HBR-%Y-%m-%d-%H-%M-%S-HBR") +
                 '.json', 'wb')
        f.write(json.dumps(items))
        f.close()

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
