import unittest
from New_index import *

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_scrape_url(self):
        payload = {
            "url": "https://greychaindesign.com/about/"
        }
        response = self.client.post('/scrape', json=payload)
        self.assertEqual(response.status_code, 200)        
        self.assertIsNotNone(response.data)


    def test_get_links(self):
        payload = {
            "url": "https://greychaindesign.com/about/",
            "sentence": "GreyChain"
        }

        response = self.client.post('/getLinks', json=payload)

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.data)

if __name__ == '__main__':
    unittest.main()



