import json

class jsontest(object):

    def __init__(self):
        self.itemMap = {}
        with open('pv.json', 'rU') as f:
            for line in f:
                jsdata = json.loads(line)
                self.itemMap[jsdata['itemNo']] = jsdata

    def inStock(self, itemNo): 
        item = self.itemMap[itemNo]
        return item and item['inStock'] == True

x = jsontest()
print 'ALL4000MR-01 * instock = %s' % x.inStock('ALL4000MR-01 *')
print 'ALLHER-01  * instock = %s' % x.inStock('ALLHER-01  *')

