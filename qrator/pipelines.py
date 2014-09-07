# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from pyes import ES
from bs4 import BeautifulSoup
from dateutil.parser import parse

class QratorPipeline(object):
    def process_item(self, item, spider):
        return item

class JsonWriterPipeline(object):

    def __init__(self):
        self.file = open('items.jl', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

class ElasticSearchPipeline(object):

    def __init__(self):    
        self.conn = ES('localhost:9200') 
        # self.file = open('urls.csv', 'wb')
        # self.file.write('spider,url' + '\n')

    def process_item(self, item, spider):        
        #self.file.write(spider.name + ',' + spider.start_urls[0] + '\n')
        self.conn.index(dict(item), "qrator", spider.name)
        return item

class FilterHTMLPipeline(object):
    
    def process_item(self, item, spider):
        if spider.name == 'nytInternationalHome' or spider.name == 'nytHome':
            item['description'] = BeautifulSoup(item['description'][0]).text
            #item['description'] = item['description'][0]
            item['title'] = item['title'][0]
            item['link'] = item['link'][0]
            item['published'] = parse(item['published'][0]).isoformat()
        elif spider.name == 'TechCrunch':
            #item['description'] = BeautifulSoup(item['description']).text
            item['title'] = item['title']
            item['published'] = parse(item['published']).isoformat()
        elif spider.name == 'HBR':
            item['title'] = item['title'][0]
            item['description'] = item['description'][0]
            item['link'] = item['link'].pop()
            #item['origlink'] = item['origlink'][0]
            item['ID'] = item['ID'][0]
            item['published'] = parse(item['published'][0]).isoformat()
        elif spider.name == 'DiscoverMag':
            item['published'] = parse(item['published']).isoformat()
        
        return item
