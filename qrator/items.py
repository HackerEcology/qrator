# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class CraigslistSampleItem(Item):
    title = Field()
    link = Field()

class HBRAuthor(Item):
    name = Field()
    uri = Field()
    
class HBRContributor(Item):
    name = Field()
    uri = Field()

class HBRItem(Item):
    title = Field()
    link = Field()    
    ID = Field()    
    updated = Field()    
    summary = Field()    
    author = Field()        
    contributor = Field()
    category = Field()
    content = Field()
    origlink = Field()

class NYItem(Item):
    title = Field()
    link = Field()    
    description = Field()
    category = Field()
    pubDate = Field()

class MitTechItem(Item):
    title = Field()
    link = Field()    
    description = Field()
    category = Field()
    pubDate = Field()

class FTItem(Item):
    title = Field()
    link = Field()    
    description = Field()
    pubDate = Field()


