import os.path
import tornado.web
from testexample.ticker_handler import TickerHandler, blockchain_info_loader

tornado.locale.load_translations(os.path.join(os.path.dirname(__file__), 'translations'))

class ExampleApp(tornado.web.Application):
    def __init__(self, *args, **kwargs):
        tornado.web.Application.__init__(self,
                                         [(r"/", tornado.web.RedirectHandler, dict(url="/ticker")),
                                          (r"/ticker", TickerHandler, dict(data_loader=blockchain_info_loader)),
                                          ],
                                         *args, **kwargs)
