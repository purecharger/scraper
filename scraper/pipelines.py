import json
import pprint
from scrapy import signals
from scrapy.exceptions import DropItem

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

    def process_item(self, item, spider):
        if item['inStock'] and not self.inStock(item['itemNo']):
            return item
#        else:
#            raise DropItem('stock has not changed for %s' % item['itemNo'])
            
class EmailPipeline(object):

    def __init__(self):
        self.items = []

    def process_item(self, item, spider):
        #print 'EmailPipeline - Found in stock item: %s' % item
        if item is not None:
            self.items.append(item)

    def close_spider(self, spider):
        pprint.pprint(self.items)
