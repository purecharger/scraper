# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class PVItem(Item):
    itemNo = Field()
    desc = Field()
    inStock = Field()
    price = Field()

