import tornado.testing
from testexample import ExampleApp

class TestExampleApp(tornado.testing.AsyncHTTPTestCase,
                     tornado.testing.LogTrapTestCase):

    def get_app(self):
        return ExampleApp()

    def test_home(self):
        response = self.fetch('/')
        self.assertEqual(response.code, 200)

    def test_ticker(self):
        response = self.fetch('/ticker')
        self.assertEqual(response.code, 200)
