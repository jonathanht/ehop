import json
import requests
from twilio.rest import Client
import sys

# coords of UTC

x = 33.650160  # latitude
y = -117.838957  # longitude

# Construct the class

class RestaurantLocator:

    def __init__(self, x, y, filters: list):
        self._x = x
        self._y = y
        self._BaseURL = "https://api.yelp.com/v3/businesses/search"
        self._ID = "" # Client ID
        self._API = "" # API Key
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
        self.recommendations = []

        self.radius = 100  # 1000m~0.62 miles


#   Constructs the url using API,

    def constructData(self):
        req = requests.get(self._BaseURL, params=self.param, headers=self.headers)
        data = json.loads(req.text)

        return data

#   Filters results from Yelp API

    def filterResults(self, data):
        retList = []
        filteredList = []
        print(data)
        for item in data['businesses']:
            if item['distance'] < self.radius:
                innerList = []
                innerList2 = []
                filtered = False
                for cdicts in item['categories']:
                    innerList.append(cdicts['alias'])
                    innerList2.append(cdicts['title'])
                for filter in innerList:
                    #changed here!!!
                    if filter in self.filters.keys():
                        filtered = True
                for title in innerList2:
                    if title in self.filters.values():
                        filtered = True
                if filtered:
                    filteredList.append((item['name'], item['price'], item['distance']))
                else:
                    retList.append((item['name'], item['price'], item['distance']))

            self.recommendations = retList

        return retList, filteredList

# Provides alternatives to the user's bad food choice

    def suggestions(self, healthies):
        #returns restaurant name and distance
        retval = sorted(healthies, key = lambda x: x[2], reverse = True)
        if (retval == []):
            return set()
        return (retval[0][0], retval[0][2])


# Main function

def yelp(lat, long, phonenum):
    # DANGER! This is insecure. See http://twil.io/secure
    #print("these are the data:", long,lat,phonenum)
    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)

    tester = RestaurantLocator(lat, long, ['fast food', 'desserts'])
    m = tester.constructData()
    healthy, unhealthy = tester.filterResults(m)
    suggestion = tester.suggestions(healthy)
    print("checking if need to send")
    if (len(unhealthy) > 0):
        print("system sending messages")
        if (len(suggestion) != 0):
            print('Hey you must be hungry! But there are better alternatives around!\nTry {} just {}m away!'.format(suggestion[0],suggestion[1]))
            message = client.messages \
                .create(
                body='Hey you must be hungry! But there are better alternatives around!\nTry {} just {}m away!'.format(suggestion[0],suggestion[1]),
                from_='+1',
                media_url=['https://i.imgur.com/Cd6JPow.jpg'],
                to= '+1'
            )
            
        else:
            print('Try to be mindful when you order later. Have a nice meal!')
            message = client.messages \
                .create(
                body='Try to be mindful when you order later. Have a nice meal!',
                from_='+1',
                media_url=['https://i.imgur.com/Cd6JPow.jpg'],
                to= '+1'
            )
            
        #print(message.status)

    
