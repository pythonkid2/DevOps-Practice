import unittest
import requests

class TestWebsiteConnection(unittest.TestCase):

    def test_website_load(self):
        response = requests.get("https://atg.world")
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
