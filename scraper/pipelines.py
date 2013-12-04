import json
import pprint
from scrapy import signals
from scrapy.exceptions import DropItem
from scrapy.mail import MailSender

class ScraperPipeline(object):
    def process_item(self, item, spider):
        return item

class StockCheckerPipeline(object):
    
    def __init__(self):
        self.itemMap = {}
        with open('pv.json', 'rU') as f:
            for line in f:
                jsdata = json.loads(line)
                self.itemMap[jsdata['itemNo']] = jsdata

    def inStock(self, itemNo):    
        item = self.itemMap[itemNo]
        return item and item['inStock'] == True

    def updateStock(self, itemNo, inStock):
        item = self.itemMap[itemNo]
        item['inStock'] = inStock

    def process_item(self, item, spider):
        self.updateStock(item['itemNo'], item['inStock'])
        if item['inStock'] and not self.inStock(item['itemNo']):
            return item

    def close_spider(self, spider):
        with open('pv.json.new', 'w') as outfile:
            for key in self.itemMap:
                json.dump(self.itemMap[key], outfile)
                outfile.write('\n')
            
class EmailPipeline(object):

    def __init__(self):
        self.items = []

    def process_item(self, item, spider):
        #print 'EmailPipeline - Found in stock item: %s' % item
        if item is not None:
            self.items.append('%s - price=$%s' % (item['desc'], item['price']))

    def close_spider(self, spider):
        mailer = MailSender()
        mailer.send(to=["rnideffer@gmail.com"], subject="PowderValley New In-Stock", body=pprint.pformat(self.items))
