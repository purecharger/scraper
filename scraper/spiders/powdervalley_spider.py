from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from scraper.items import PVItem

class PowderValleySpider(BaseSpider):
    name = "powdervalley"
    allowed_domains = ["powdervalleyinc.com"]
    start_urls = [
        "http://www.powdervalleyinc.com/alliant.shtml"
#        "http://www.powdervalleyinc.com/hodgdon.shtml",
#        "http://www.powdervalleyinc.com/CCIprimers.shtml",
#        "http://www.powdervalleyinc.com/WINprimers.shtml",
#        "http://www.powdervalleyinc.com/REMprimers.shtml"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        rows = hxs.select('//form[@name="itemsform"]/table/tr')
        items = {} 
        for row in rows:
            values = row.select('td/font/text()').extract()
            if len(values) == 4:
                item = PVItem()
                item['itemNo'] = values[0]
                item['desc' ]= values[1]

                if values[2] == 'Yes':
                    item['inStock'] = True
                else:
                    item['inStock'] = False

                item['price'] = float(values[3][1:])

                items[values[0]] = item

        print items
        return items

