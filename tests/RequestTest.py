import unittest
import requests
import json


class RequestTest(unittest.TestCase):
    def test_get(self):
        r = requests.get('http://httpbin.org/ip')

        self.assertEqual(r.headers['Server'], 'nginx')

    def test_get_with_params(self):
        r = requests.get('http://httpbin.org/get', params={"a": 1})

        self.assertEqual(r.json()['args']['a'], '1')

    def test_post(self):
        r = requests.post('http://httpbin.org/post', data='xxx')

        self.assertEqual(r.json()['data'], 'xxx')

    def test_post(self):
        r = requests.post('http://httpbin.org/post', json={"a": 1})
        self.assertEqual(json.loads(r.json()['data']), {"a": 1})

    def test_session(self):
        s = requests.Session()

        s.get('http://httpbin.org/cookies/set/x/1')

        r = s.get('http://httpbin.org/cookies')

        self.assertEqual(r.json()['cookies'], {
            "x": '1'
        })
