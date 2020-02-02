import json
import requests


# coords of UTC

x = 33.650160  # latitude
y = -117.838957  # longitude

# Construct the class

class RestaurantLocator:

    def __init__(self, x, y, filters: list):
        self._x = x
        self._y = y
        self._BaseURL = "https://api.yelp.com/v3/businesses/search"
        self._ID = "1Vp1MSf8DUcnw-OjS41qzQ" # Client ID
        self._API = "ljefBWbwtGtW4FYiVXEFj5qMXQMBaL08TR1mU6uCa421ZpT7ABj060EfqL7cJQTPRpek-P6-GtmiskfuwihuduS88ie0KDa7dIt2nFDLnQCjWni0aDkcdghjW0M1XnYx" # API Key
        self.headers = {'Authorization': 'Bearer %s' % self._API}
        self.param = {'term': 'restaurant, fast food, desserts', 'latitude': self._x, 'longitude': self._y}
        self.filters = {'fast food': 'Fast Food',
                        'burgers': 'Burgers',
                        'desserts': 'Desserts',
                        'hot dog': 'Hot Dog',
                        'pizza': 'Pizza',
                        'barbecue': 'Barbeque',
                        'chicken shop': 'Chicken Shop',
                        'chicken wings': 'Chicken Wings'}
        self.userFilters = {}
        for item in filters:
            if item in self.filters.keys():
                self.userFilters[item] = self.filters[item]

        self.radius = 1000  # ~0.62 miles


#   Constructs the url using API,

    def constructData(self):
        req = requests.get(self._BaseURL, params=self.param, headers=self.headers)
        data = json.loads(req.text)

        return data

#   Filters results from Yelp API

    def filterResults(self, data):
        retList = []
        filteredList = []
        for item in data['businesses']:
            if item['distance'] < self.radius:
                innerList = []
                innerList2 = []
                filtered = False
                for cdicts in item['categories']:
                    innerList.append(cdicts['alias'])
                    innerList2.append(cdicts['title'])
                for filter in innerList:
                    if filter in self.userFilters.keys():
                        filtered = True
                for title in innerList2:
                    if title in self.userFilters.values():
                        filtered = True
                if filtered:
                    filteredList.append((item['name'], item['distance']))
                else:
                    retList.append((item['name'], item['distance']))

        return retList, filteredList


# Main function

if __name__ == "__main__":
    tester = RestaurantLocator(x, y, ['fast food', 'desserts'])
    m = tester.constructData()
    p, q = tester.filterResults(m)
    for item in p:
        print(item)
    print("****")
    for item in q:
        print(item)

