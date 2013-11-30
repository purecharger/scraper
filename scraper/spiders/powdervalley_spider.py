from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy import log

from scraper.items import PVItem

class PowderValleySpider(BaseSpider):
    name = "powdervalley"
    allowed_domains = ["powdervalleyinc.com"]
    start_urls = [
        "http://www.powdervalleyinc.com/alliant.shtml",
        "http://www.powdervalleyinc.com/hodgdon.shtml",
        "http://www.powdervalleyinc.com/CCIprimers.shtml",
        "http://www.powdervalleyinc.com/WINprimers.shtml",
        "http://www.powdervalleyinc.com/REMprimers.shtml"
    ]

    def parse(self, response):
        sel = Selector(response)
        rows = sel.xpath('//form[@name="itemsform"]/table/tr')
        items = []
        for row in rows:
            values = row.xpath('td/font/text()').extract()
            if len(values) >= 4:
                item = PVItem()
                item['itemNo'] = values[0]
                item['desc' ]= values[1]

                if values[2] == 'Yes':
                    item['inStock'] = True
                else:
                    item['inStock'] = False

                try:
                    item['price'] = float(values[3][1:])
                except ValueError:
                    item['price'] = 0
                    log.msg('ValueError! values=[%s] values[3]=%s' % (values, values[3]))

                items.append(item)

        return items

