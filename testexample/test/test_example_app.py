import tornado.testing
from testexample import ExampleApp

class TestExampleApp(tornado.testing.AsyncHTTPTestCase,
                     tornado.testing.LogTrapTestCase):

    def get_app(self):
        return ExampleApp()

    def test_fail(self):
        assert 0 == 1
