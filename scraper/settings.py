# Scrapy settings for scraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'scraper'

SPIDER_MODULES = ['scraper.spiders']
NEWSPIDER_MODULE = 'scraper.spiders'

#FEED_URI = 'file:///tmp/pv.json'
#FEED_FORMAT = 'jsonlines'

# Set, int value is order to run component in, low to high (valid: 0-1000)
ITEM_PIPELINES = {
        'scraper.pipelines.StockCheckerPipeline' : 100,
        'scraper.pipelines.EmailPipeline' : 200
}

MAIL_FROM = 'ryan@powdervalley-inStock.com'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scraper (+http://www.yourdomain.com)'
