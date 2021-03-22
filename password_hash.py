import requests
import unittest
import socket

class Test_Password_Hash(unittest.TestCase):

    HOST = '127.0.0.1'
    PORT = 8088

    def setUp(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.HOST, self.PORT))

    def test_post_password(self):
        URL = 'http://' + f'{self.HOST}' + f':{self.PORT}' + '/hash'
        DATA = {'password': 'angrymonkey'}

        r = requests.post(url=str(URL), json={'json_payload': DATA})
        print(r.text)
        assert r.status_code == 200

    def test_get_encoded_password(self):
        URL = 'http://' + f'{self.HOST}' + f':{self.PORT}' + '/hash/1'

        r = requests.get(url=URL)
        print(r.text)
        assert r.status_code == 200

    def test_get_the_stats(self):
        URL = 'http://' + f'{self.HOST}' + f':{self.PORT}' + '/stats'

        r = requests.get(url=URL)
        print(r.text)
        assert r.status_code == 200

    def tearDown(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.close()

if __name__ == '__main__':
    unittest.main()
