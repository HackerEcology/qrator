# Scrapy settings for qrator project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'qrator'

SPIDER_MODULES = ['qrator.spiders']
NEWSPIDER_MODULE = 'qrator.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'qrator (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
    # 'qrator.pipelines.JsonWriterPipeline': 10,
    'qrator.pipelines.FilterHTMLPipeline': 11,
    'qrator.pipelines.ElasticSearchPipeline': 12,
}
