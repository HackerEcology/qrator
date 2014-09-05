from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from scrapy import log, signals
from scrapy.utils.project import get_project_settings
from scrapy.command import ScrapyCommand

from qrator.spiders.newscrawlers import \
    CraigsListSpider,\
    MitTechSpider,\
    NYHomeSpider,\
    NYInternationalHomeSpider,\
    FinancialTimeSpider,\
    HBRSpider,\
    HNSpider,\
    DiscoverMagSpider,\
    TechCrunchSpider
#ArtistsSpider,\
#MashableSpider,\

# class Command(ScrapyCommand):

#     requires_project = True

#     def syntax(self):
#         return '[options]'

#     def short_desc(self):
#         return 'Runs all of the spiders'

#     def run(self, args, opts):
#         settings = get_project_settings()

#         for spider_name in self.crawler.spiders.list():
#             crawler = Crawler(settings)
#             crawler.configure()
#             spider = crawler.spiders.create(spider_name)
#             crawler.crawl(spider)
#             crawler.start()

#         self.crawler.start()

# spiders init
CRAIG = NYHomeSpider()
# MIT_TECH = MitTechSpider()
# NYT_HOME = NYHomeSpider()
# NYT_INT_HOME = NYInternationalHomeSpider()
# FT = FinancialTimeSpider()
# HBR = HBRSpider()
# HN = HNSpider()
# DISCOVER_MAG = DiscoverMagSpider()
# TC = TechCrunchSpider()

# config init
settings = get_project_settings()
crawler = Crawler(settings)
crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
crawler.configure()

# crawler init
crawler.crawl(CRAIG)
# crawler.crawl(MIT_TECH)
# crawler.crawl(NYT_HOME)
# crawler.crawl(NYT_INT_HOME)
# crawler.crawl(FT)
# crawler.crawl(HBR)
# crawler.crawl(HN)
# crawler.crawl(DISCOVER_MAG)
# crawler.crawl(TC)

# crawler start
crawler.start()
log.start()
log.msg('Reactor activated...')
reactor.run()
log.msg('Reactor stopped.')
