import json

filename = 'pv.json'

class ItemStore(object):

    def __init__(self):
        self.itemMap = {}
        with open(filename, 'rU') as f:
            for line in f:
                jsdata = json.loads(line)
                self.itemMap[jsdata['itemNo']] = jsdata

    def inStock(self, itemNo): 
        item = self.itemMap[itemNo]
        return item and item['inStock'] == True

    def getItem(self, itemNo):
        return self.itemMap[itemNo]

    def update(self, item):
        self.itemMap[item['itemNo']] = item

    def write(self):
        with open(filename, 'w') as outfile:
            for key in self.itemMap:
                json.dump(self.itemMap[key], outfile)
                outfile.write('\n')

