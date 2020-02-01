import json
import requests


# coords of UTC

x = 33.6523 # latitude
y = -117.8341 # longitude

# Construct the class

class RestaurantLocator:

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._BaseURL = "https://api.yelp.com/v3/businesses/search"
        self._ID = "1Vp1MSf8DUcnw-OjS41qzQ" # Client ID
        self._API = "ljefBWbwtGtW4FYiVXEFj5qMXQMBaL08TR1mU6uCa421ZpT7ABj060EfqL7cJQTPRpek-P6-GtmiskfuwihuduS88ie0KDa7dIt2nFDLnQCjWni0aDkcdghjW0M1XnYx" # API Key
        self.headers = {'Authorization': 'Bearer %s' % self._API}
        self.param = {'term': 'fast food', 'latitude': self._x, 'longitude': self._y}
        self.filters = ['fast food', 'burgers', 'desserts']
        self.titles = ["Fast Food", "Burgers", "Desserts"]
        self.radius = 1500

#   Constructs the url using API,

    def constructData(self):
        #retList = []
        req = requests.get(self._BaseURL, params=self.param, headers=self.headers)
        #print('The status code is {}'.format(req.status_code))
        data = json.loads(req.text)

        return data

#   Filters results from Yelp API

    def filterResults(self, data):
        retList = []
        for item in data['businesses']:
            if item['distance'] < self.radius:
                innerList = []
                innerList2 = []
                filtered = False
                for cdicts in item['categories']:
                    innerList.append(cdicts['alias'])
                    innerList2.append(cdicts['title'])
                for filter in innerList:
                    if filter in self.filters:
                        filtered = True
                for title in innerList2:
                    if title in self.titles:
                        filtered = True
                if filtered:
                    pass
                else:
                    retList.append((item['name'], item['distance']))
        for item in retList:
            print(item)
        return retList



if __name__ == "__main__":
    tester = RestaurantLocator(x, y)
    m = tester.constructData()
    tester.filterResults(m)

