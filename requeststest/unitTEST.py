import requests
import unittest


hwapi = "http://106.14.41.136:7076"

class Testchoujiang(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url = hwapi +"/avatar_api/amethyst_lottery"
        cls.uid = 120934049
        cls.num = 10


    def test_choujiang(self):
        data = {
            "uid":self.uid,
            "num":self.num
        }
        header = {
            "Content-Type":"application/x-www-form-urlencoded"
        }

        res = requests.post(self.url,headers = header,data = data).json()
        print(res)
        assert res['code'] == 200

if __name__ == '__main__':  
    unittest.main()
    

