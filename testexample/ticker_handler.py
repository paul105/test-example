import json
import tornado.gen
import tornado.web
import tornado.httpclient
from babel.numbers import format_currency

@tornado.gen.coroutine
def blockchain_info_loader():
    http_client = tornado.httpclient.AsyncHTTPClient()
    response = yield http_client.fetch('https://blockchain.info/ticker')
    if response.error:
        return None
    return json.loads(response.body.decode('utf-8'))

@tornado.gen.coroutine
def extract_localized_data(rates, locale):
    return [format_currency(value['last'], currency, locale=locale) for (currency, value) in rates.items()]

class TickerHandler(tornado.web.RequestHandler):

    def initialize(self, data_loader):
        self.data_loader = data_loader

    @tornado.gen.coroutine
    def get(self):
        rates = yield self.data_loader()
        locale = self.get_browser_locale()
        rates = yield extract_localized_data(rates, locale.code)
        self.render("templates/ticker.html", title=locale.translate("Bitcoin prices"), items=rates)
