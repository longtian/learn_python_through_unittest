from copy import deepcopy
import unittest
import sys


class LibTest(unittest.TestCase):
    # python2 默认字符编码是 ascii
    def test_defaultEncoding(self):
        self.assertEqual(sys.getdefaultencoding(), 'utf-8')

    def test_defaultEncode(self):
        u = b'\xe4\xbd\xa0\xe5\xa5\xbd'
        self.assertEqual(str(type(u)), "<class 'bytes'>")
        self.assertEqual(u.decode('utf-8'), '你好')

    def test_deepcopy(self):
        a = {"name": "z", "country": {"name": "Brazil"}}
        b = deepcopy(a)
        b["country"]["name"] = "Chine"
        self.assertEqual(a["country"]["name"], "Brazil")
