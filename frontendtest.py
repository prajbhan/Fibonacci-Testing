import unittest
import requests

class APITests(unittest.TestCase):
    def test_frontendurl(self):

        r = requests.get("http://ec2-52-35-41-144.us-west-2.compute.amazonaws.com/")
        self.assertEquals(r.status_code, 200)     

    def test_bad_url(self):
        r = requests.get("http://ec2-52-35-41-144.us-west-2.compute.amazonaw.com/")
        self.assertEquals(r.status_code, 404)


if __name__ == '__main__':
    unittest.main()
