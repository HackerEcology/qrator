from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from scrapy import log, signals
from scrapy.utils.project import get_project_settings
#from scrapy.command import ScrapyCommand
#from pdb import set_trace

# from qrator.spiders.newscrawlers import \
#     CraigsListSpider,\
#     MitTechSpider,\
#     NYHomeSpider,\
#     NYInternationalHomeSpider,\
#     HBRSpider,\
#     HNSpider,\
#     DiscoverMagSpider,\
#     TechCrunchSpider
# # FinancialTimeSpider,\
# # ArtistsSpider,\
# # MashableSpider,\

# config init
settings = get_project_settings()
crawler = Crawler(settings)

def setup_crawler(spider):
    #spider = FollowAllSpider(domain=domain)
    settings = get_project_settings()
    crawler = Crawler(settings)
    spider = crawler.spiders.create(spider_name)
    crawler.configure()
    crawler.crawl(spider)
    crawler.start()

#crawler.signals.connect(reactor.stop, signal=signals.spider_closed)

log.start()
for spider_name in crawler.spiders.list():
    setup_crawler(spider_name)
log.msg('Reactor activated...')
reactor.run()
#crawler.signals.disconnect(reactor.stop, signal=signals.spider_closed)
log.msg('Reactor stopped.')
