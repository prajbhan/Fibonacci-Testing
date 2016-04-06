import unittest
import requests

class APITests(unittest.TestCase):
    def test_fibonaccinumber(self):
        r = requests.get("http://localhost:5000/api/fibonaaci/1")
        self.assertEquals(r.status_code, 200)     

   # def test_bad_url(self):
    #    r = requests.get("http://ec2-52-11-90-237.us-west-2.compute.amazonaws.com/")
     #   self.assertEquals(r.status_code, 404)


if __name__ == '__main__':
    unittest.main()
