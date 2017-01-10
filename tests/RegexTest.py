import unittest
import re


class RegexTest(unittest.TestCase):
    def test_compile(self):
        # 需要加 r 么？
        number = re.compile('^\d*$')

        # 如何判断一个实例是不是正则表达式
        # http://stackoverflow.com/questions/6102019/type-of-compiled-regex-object-in-python
        # self.assertTrue(isinstance(number, typing.re.Pattern))

        self.assertTrue(number.match('123'))

    def test_match(self):
        number = re.compile('(\d+)(\w)')
        m = number.match('12ab34')

        self.assertEqual(m.group(), '12a')
        self.assertEqual(m.group(0), '12a')
        self.assertEqual(m.group(1), '12')
        self.assertEqual(m.group(2), 'a')

    def test_match_search_difference(self):
        """
        match 从头查找，search 所有位置
        """
        number = re.compile('\d+')

        m1 = number.match('a12b')
        m2 = number.search('a12b')

        self.assertFalse(m1)
        self.assertTrue(m2)

    def test_spit(self):
        self.assertEqual(re.split('\d+', '12ab34de'), ['', 'ab', 'de'])

    def test_findall(self):
        self.assertEqual(re.findall(r'\d+', '12ab34'), ['12', '34'])

    def test_sub(self):
        self.assertEqual(re.sub('\d', '_', '1x23'), '_x__')
