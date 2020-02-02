#import the yelp api
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
import json
class Feedback(RequestHandler):
    def get(self):
        print(self.request.body)
        data = json.loads(self.request.body)
        print(data)
        self.write()
def make_app():
    urls = [
        (r"/feedback", Feedback),
    ]
    return Application(urls, debug=True)
if __name__ == '__main__':
    # r = requests.put(f"https://a.klaviyo.com/api/v1/person/QDT7JY?api_key={cr.klaviyo['private_key']}&sales_amount=10")
    # print(r.status_code)
    # print(r.text)
    app = make_app()
    app.listen(8888)
    IOLoop.current().start()