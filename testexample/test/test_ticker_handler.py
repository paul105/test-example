import json
import os.path
import tornado.gen
import tornado.web
import tornado.testing
from testexample.ticker_handler import TickerHandler

RATES_FIXTURE = {}
with open(os.path.join(os.path.dirname(__file__), 'fixtures/ticker.json')) as f:
    RATES_FIXTURE = json.load(f)

@tornado.gen.coroutine
def dummy_loader():
    return RATES_FIXTURE

class TestTickerHandler(tornado.testing.AsyncHTTPTestCase,
                        tornado.testing.LogTrapTestCase):

    def get_app(self):
        # instead of connecting to the API over Internet this test
        # uses a fixture from a static file
        return tornado.web.Application([(r"/", TickerHandler, dict(data_loader=dummy_loader))])

    def test_ticker_en(self):
        response = self.fetch('/', headers={'Accept-Language': 'en_US'})
        self.assertEqual(response.code, 200)
        body = response.body.decode('utf-8')
        self.assertIn('Bitcoin prices', body)
        self.assertIn('478.68$', body)

    def test_ticker_pl(self):
        response = self.fetch('/', headers={'Accept-Language': 'pl_PL'})
        self.assertEqual(response.code, 200)
        body = response.body.decode('utf-8')
        self.assertIn('Ceny Bitcoina', body)
        # a non-braking space
        self.assertIn('478,68' + b'\xc2\xa0'.decode('utf-8') + 'USD', body)

