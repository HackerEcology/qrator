# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from pyes import ES

DUMP = "/media/F/workspace/A_PERSONAL_projects/HackerEcology/qrator/dumps/"

class QratorPipeline(object):
    def process_item(self, item, spider):
        return item

class JsonWriterPipeline(object):

    def __init__(self):
        self.file = open(DUMP+'items.jl', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

class ElasticSearchPipeline(object):

    def __init__(self):    
        self.conn = ES('localhost:9200')
        #self.conn.indices.create_index('qrator')

    def process_item(self, item, spider):
        self.conn.index(dict(item), "qrator", "spider")
        return item
