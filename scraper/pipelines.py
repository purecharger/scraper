# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import json
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
        else:
            raise DropItem("Stock status has not changed for item: %s" % item['itemNo'])
            
