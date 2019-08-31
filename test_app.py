import unittest
import app

class TestApp(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()


    def test_app(self):
        result = self.app.get('/')
        self.assertEqual(result.status, '200 OK')
        self.assertEqual(result.data, b'Hello World')


if __name__ == '__main__':
    unittest.main()