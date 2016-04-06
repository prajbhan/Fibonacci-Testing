import unittest
import requests

class APITests(unittest.TestCase):
    def test_fibonaccinumber(self):
        r = requests.get("http://localhost:5000/api/fibonaaci/1")
        self.assertEquals(r.status_code, 200)     

    def test_fibonaccinumber1(self):
        r = requests.get("http://ec2-52-35-41-144.us-west-2.compute.amazonaws.com:5000/api/fibonacci/2")
        self.assertEquals(r.status_code, 200)

    def test_character (self):
        r = requests.get("http://ec2-52-35-41-144.us-west-2.compute.amazonaws.com:5000/api/fibonacci/A")
        self.assertEquals(r.status_code, 200)

    def test_negativeint(self):
        r = requests.get("http://ec2-52-35-41-144.us-west-2.compute.amazonaws.com:5000/api/fibonacci/-2")
        self.assertEquals(r.status_code, 200)

    def test_specialcharacter(self):
        r = requests.get("http://ec2-52-35-41-144.us-west-2.compute.amazonaws.com:5000/api/fibonacci/#")
        self.assertEquals(r.status_code, 200)

    def test_emptystring (self):
        r = requests.get("http://ec2-52-35-41-144.us-west-2.compute.amazonaws.com:5000/api/fibonacci/")
        self.assertEquals(r.status_code, 200)

if __name__ == '__main__':
    unittest.main()
