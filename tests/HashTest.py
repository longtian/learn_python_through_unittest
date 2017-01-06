import unittest
import base64
import hashlib


class HashTest(unittest.TestCase):
    def test_base64(self):
        self.assertEqual(base64.b64encode(b'123456'), b'MTIzNDU2')
        self.assertEqual(base64.b64decode(b'MTIzNDU2'), b'123456')

    def test_md5(self):
        def md5(string):
            return hashlib.md5(string.encode('utf-8')).hexdigest()

        self.assertEqual(md5('123456'), 'e10adc3949ba59abbe56e057f20f883e')

    def test_sha1(self):
        def sha(string):
            return hashlib.sha1(string.encode('utf-8')).hexdigest()

        self.assertEqual(sha('123456'), '7c4a8d09ca3762af61e59520943dc26494f8941b')
