"""
crawler for various news agencies.
"""

# export using: 
# $ scrapy crawl nytHome -o items.json -t json
# for csv/xml/.. simply substitue types

# API's
# http://developer.nytimes.com/docs
# http://developer.usatoday.com/

from scrapy.spider import Spider #, BaseSpider
import scrapy.http
from scrapy.selector import HtmlXPathSelector, Selector

from qrator.items import \
    CraigslistSampleItem, \
    NYItem, \
    HBRItem, HBRContributor, HBRAuthor, \
    FTItem, HackerNewsItem, TechCrunchItem, \
    DiscoverMagItem

import os
import re
import json
import time

# print items[0]
# if os.path.exists('data'):
#     pass
# else:
#     os.mkdir('data')
# f = open('data/' +
#          time.strftime("NYHome-%Y-%m-%d-%H-%M-%S-NYHome") +
#          '.json', 'wb')
# f.write(json.dumps(items))
# f.close()

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


# class CraigsListSpider(Spider):
    
#     '''
#     Craigs List.
#     '''
#     name = "craig"
#     allowed_domains = ["craigslist.org"]
#     start_urls = ["http://sfbay.craigslist.org/npo/"]

#     def parse(self, response):
#         sel = Selector(response)
#         titles = sel.xpath("//span[@class='pl']")
#         #titles = sel.select("//span[@class='pl']")
#         items = []
#         for titles in titles:
#             item = CraigslistSampleItem()
#             item["title"] = titles.xpath("a/text()").extract()
#             item["link"] = titles.xpath("a/@href").extract()
#             items.append(item)
#         return items


class MitTechSpider(Spider):

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
                except IndexError:
                    continue
                # print item2
        for key, value in items.iteritems():
            print "\nType: %s\nContent: %s\n" % (key, value)
        # return items


class NYHomeSpider(Spider):

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
            item = NYItem()
            item["title"] = header.xpath('title/text()').extract()
            item["link"] = header.xpath('link/text()').extract()
            item['description'] = header.xpath('description/text()').extract()
            item['category'] = header.xpath('category/text()').extract()
            item['published'] = header.xpath('pubDate/text()').extract()
            items.append(item)
        return items

        
class NYInternationalHomeSpider(Spider):

    '''
    New York Times Internation-Home.
    '''
    name = "nytInternationalHome"
    allowed_domains = ["nytimes.com"]
    start_urls = ["http://rss.nytimes.com/services/xml/rss/nyt/InternationalHome.xml"]

    def parse(self, response):
        sel = Selector(response)
        headers = sel.xpath("//item")
        items = []
        for header in headers:
            item = NYItem()
            item["title"] = header.xpath('title/text()').extract()
            item["link"] = header.xpath('link/text()').extract()
            item['description'] = header.xpath('description/text()').extract()
            item['category'] = header.xpath('category/text()').extract()
            item['published'] = header.xpath('pubDate/text()').extract()
            items.append(item)

        return items


# class FinancialTimeSpider(Spider):

#     '''
#     Financial Times All.
#     '''
#     name = "ft"
#     allowed_domains = ["ft.com"]
#     start_urls = ["http://www.ft.com/rss"]

#     '''
#     Need to request rss for every url
#     '''

#     def parse(self, response):        
#         sel = Selector(response)
#         rss_items = [x.xpath('text()').extract() + x.xpath('@href').extract() \
#                      for x in sel.xpath("//a") \
#                      if x.xpath('@href').extract()[0].find('/rss/')!=-1]
#         for item in rss_items:
#             # print item[1].encode('ascii', errors='backslashreplace')
#             # self.parse_SingleRSS(item[1].encode('ascii', errors='backslashreplace'))
#             yield scrapy.http.Request(url=item[1].encode('ascii', errors='backslashreplace'),callback=self.parse1)
#             # print sel_item
#             # print sel_item.extract()
#             # print sel_item.extract()
#             # xmlItems = sel_item.xpath("//title")
#             # print xmlItems.extract()
#         # for rss in rss_items:
#             # print rss.xpath('href').extract()

#     def parse_SingleRSS(self,rssString):
#         # print rssString
#         return scrapy.http.Request(url=rssString,callback=self.parse1)

#     def parse1(self, response):
#         sel = Selector(response)
#         headers = sel.xpath("//item")
#         items = []
#         for header in headers:
#             item = FTItem()
#             item["title"] = header.xpath('title/text()').extract()[0]
#             item["link"] = header.xpath('link/text()').extract()[0]
#             item['description'] = header.xpath('description/text()').extract()[0]
#             item['published'] = header.xpath('pubDate/text()').extract()[0]
#             items.append(item)
#         return items


class HBRSpider(Spider):

    '''
    Harvard Business Review.
    '''
    name = "HBR"
    allowed_domains = ["harvardbusiness.org"]
    start_urls = ["http://feeds.harvardbusiness.org/harvardbusiness"]

    def parse(self, response):
        sel = HtmlXPathSelector(response) # Selector() returns [] for '//entry'
        entries = sel.xpath('//entry')
        items = []

        for entry in entries:
            item = HBRItem()
            item['title'] = entry.xpath('title/text()').extract()
            item['ID'] = entry.xpath('id/text()').extract()
            item['published'] = entry.xpath('updated/text()').extract()
            item['description'] = entry.xpath('summary/text()').extract()
            # author is nested with [name, uri]
            author = HBRAuthor()
            author['name'] = entry.xpath('author/name/text()').extract()
            author['uri'] = entry.xpath('author/uri/text()').extract()
            item['author'] = dict(author)
            # contributor is nested with [name, uri]
            # contrib = HBRContributor()
            # contrib['name'] = entry.xpath('contributor/name/text()').extract()
            # contrib['uri'] = entry.xpath('contributor/uri/text()').extract()
            #item['contributor'] = [dict(contrib)]
            item['category'] = entry.xpath('category/@term').extract()
            # item['content'] = entry.xpath('content/text()').extract()
            item['link'] = entry.xpath('origlink/text()').extract()
            items.append(item)

        return items

        
class HNSpider(Spider):

    '''
    Hacker News.
    '''
    name = "hackerNews"
    allowed_domains = ["ycombinator.com"]
    start_urls = ["https://news.ycombinator.com/rss"]
    def parse(self, response):
        sel = Selector(response)
        # print sel.extract()
        headers = sel.xpath('//item')
        items = []
        for header in headers:
            item = HackerNewsItem()
            item['title'] = header.xpath('title/text()').extract()[0]
            item['link'] = header.xpath('link/text()').extract()[0]
            item['comments'] = header.xpath('comments/text()').extract()[0]
            item['descriptionLink'] = header.xpath('description/text()').extract()[0]
            items.append(item)
        for item in items:
            print item
        return items

# class MitTechReviewSpider(Spider):

#     '''
#     MIT Tech Review.
#     '''
#     name = "techReview"
#     allowed_domains = ["technologyreview.com"]
#     start_urls = ["http://www.technologyreview.com/connect/#rss"]
#     def parse(self, response):
#         pass


# class BusinessInsiderSpider(Spider):

#     '''
#     Business Insider.
#     '''
#     name = "bInsider"
#     allowed_domains = ["businessinsider.com"]
#     start_urls = ["http://www.businessinsider.in/rss_feeds.cms"]
#     def parse(self, response):
#         pass


# class USATodaySpider(Spider):

#     '''
#     USA Today.
#     '''
    
#     name = "usaToday"
#     allowed_domains = ["usatoday.com"]
#     start_urls = ["http://content.usatoday.com/marketing/rss/index.aspx"]
#     def parse(self, response):
#         pass


# class LATimesSpider(Spider):

#     '''
#     LA Times.
#     '''
#     name = "laTimes"
#     allowed_domains = ["latimes.com"]
#     start_urls = ["http://www.latimes.com/la-los-angeles-times-rss-feeds-20140507-htmlstory.html"]
#     def parse(self, response):
#         pass


# class TheTimesSpider(Spider):

#     '''
#     The Times.
#     '''
#     name = "theTimes"
#     allowed_domains = ["thetimes.co.uk"]
#     start_urls = ["http://www.thetimes.co.uk/tto/feedindex/"]

#     def parse(self, response):
#         pass


# class WSJSpider(Spider):

#     '''
#     WallStreet Journal.
#     '''
#     name = "wsj"
#     allowed_domains = ["wsj.com"]
#     start_urls = ["http://online.wsj.com/public/page/rss_news_and_feeds.html"]
#     def parse(self, response):
#         pass

# class ArsTechnicaSpider(Spider):

#     '''
#     Ars Technica.
#     '''
#     name = "arsTechnica"
#     allowed_domains = ["arstechnica.com"]
#     start_urls = ["arstechnica.com/rss-feeds/"]
#     def parse(self, response):
#         pass


class TechCrunchSpider(Spider):
    '''
    TechCrunch
    '''
    name="TechCrunch"
    allowed_domains = ["techcrunch.com"]
    start_urls = ["http://feeds.feedburner.com/TechCrunch/"]
    def parse(self, response):
        sel = Selector(response)
        headers = sel.xpath("//item")
        items = []
        for header in headers:
            item = TechCrunchItem()
            item["title"] = header.xpath('title/text()').extract()[0]
            item["link"] = header.xpath('link/text()').extract()[0]
            item['description'] = header.xpath('description/text()').extract()[0]
            item['published'] = header.xpath('pubDate/text()').extract()[0]
            item['category'] = [x.xpath('text()').extract()[0] for x in header.xpath('//category')]
            #item['author'] = header.xpath('dc:creator/text()').extract()
            # item['media_thumbnail'] = header.xpath('media:thumbnail').extract()[0]
            items.append(item)
        return items
        

# class MashableSpider(Spider):
#     '''
#     Mashable: only the "next big thing"
#     '''
#     name="MashableBigThing"
#     allowed_domains = ["mashable.com"]
#     start_urls = ["http://mashable.com/category/rss/"]
#     def parse(self, response):
#         sel = Selector(response)
#         print sel.extract()

'''
Spiders for ideas

'''

'''
Spiders for science
'''

class DiscoverMagSpider(Spider):

    '''
    Discover Magazine.
    '''
    name = "DiscoverMag"
    allowed_domains = ["discovermagazine.com"]
    start_urls = ["http://feeds.feedburner.com/AllDiscovermagazinecomContent"]
    def parse(self, response):
        sel = Selector(response)
        headers = sel.xpath("//item")
        items = []
        for header in headers:
            item = DiscoverMagItem()
            item["title"] = header.xpath('title/text()').extract()[0]
            item["link"] = header.xpath('link/text()').extract()[0]
            item['description'] = header.xpath('description/text()').extract()[0]
            item['published'] = header.xpath('pubDate/text()').extract()[0]
            items.append(item)
        for item in items:
            print item
        return items

# class Spider(Spider):

#     '''
#     New York Times Internation-Home.
#     '''
#     name = "HBR"
#     allowed_domains = ["harvardbusiness.org"]
#     start_urls = ["http://feeds.harvardbusiness.org/harvardbusiness"]
#     def parse(self, response):
#         pass

'''
This is something totally random
'''

# class ArtistsSpider(Spider):

#     '''
#     Important Artists: http://www.theartwolf.com/articles/most-important-painters.htm
#     '''

#     name = "artists"
#     allowed_domains = ["theartwolf.com"]
#     start_urls = ["http://www.theartwolf.com/articles/most-important-painters.htm"]
#     def parse(self,response):
#         sel = HtmlXPathSelector(response) # Selector() returns [] for '//entry'
#         entries = sel.xpath("//div[@class='noticiacentro']")[0].xpath("//p")
#         items = []
#         for entry in entries:
#             person = {}
#             name = entry.xpath('strong/text()').extract()
#             description = entry.xpath('text()').extract()
#             if name != [] and description != []:
#                 person['name'] = name[0]
#                 person['description'] = description[1]
#                 items.append(person)
#             # print entry.extract()
#         print items
#         # f = open('artists.json', 'wb')
#         # f.write(json.dumps(items))
#         # f.close()
