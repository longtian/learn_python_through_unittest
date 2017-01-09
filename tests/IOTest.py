import unittest
import base64
import os
from os.path import join, dirname, abspath


class IOTest(unittest.TestCase):
    def test_read_try(self):
        try:
            file = open(join(dirname(__file__), '../README.md'), 'r')
            self.assertGreater(len(file.read()), 10)
        except Exception as e:
            print(e)

    def test_read_context(self):
        with open(join(dirname(__file__), '../README.md'), 'r') as file:
            self.assertGreater(len(file.read()), 10)

    def test_data_url(self):
        with open(join(dirname(__file__), '../cat_rocket.jpg'), 'rb') as file:
            image_date = file.read()
            base64_data = base64.b64encode(image_date)

            # 可以在浏览器里打开这个 url
            data_url = 'data:image/jpg;base64,' + str(base64_data, 'ascii')

            self.assertGreater(len(data_url), 100)

    def test_walk(self):
        def inspect(filename):
            print(filename)

        files = os.walk(abspath(join(dirname(__file__), '../')))

        l = [dirpath for dirpath, dirname, filenames in files]

        self.assertGreater(len(l), 0)
