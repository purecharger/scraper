from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

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
        hxs = HtmlXPathSelector(response)
        rows = hxs.select('//form[@name="itemsform"]/table/tr')
        items = []
        for row in rows:
            values = row.select('td/font/text()').extract()
            if len(values) == 5:
                item = PVItem()
                item['itemNo'] = values[0]
                item['desc' ]= values[1]
                item['inStock'] = values[2]
                item['price'] = values[3]

