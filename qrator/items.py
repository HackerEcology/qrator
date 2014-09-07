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
    published = Field()    
    description = Field()    
    author = Field()        
    contributor = Field()
    category = Field()
    content = Field()
    #origlink = Field()

class NYItem(Item):
    title = Field()
    link = Field()    
    description = Field()
    category = Field()
    published = Field()

class MitTechItem(Item):
    title = Field()
    link = Field()    
    description = Field()
    category = Field()
    published = Field()

class FTItem(Item):
    title = Field()
    link = Field()    
    description = Field()
    published = Field()

class HackerNewsItem(Item):
    title = Field()
    link = Field()
    comments = Field()
    descriptionLink = Field()

class TechCrunchItem(Item):
    title = Field()
    link = Field()
    published = Field()
    author = Field()
    category = Field()
    guid = Field()
    description = Field()
    media_thumbnail = Field()

class DiscoverMagItem(Item):
    title = Field()
    link = Field()
    published = Field()
    description = Field()
