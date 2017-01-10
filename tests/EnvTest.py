import unittest
import os


class EnvTest(unittest.TestCase):
    def test_get_path(self):
        self.assertGreater(len(os.environ['PATH']), 0)

    def test_get_with_default(self):
        self.assertEqual(os.getenv('PATHX', 'X'), 'X')
