import unittest
import calendar
from datetime import datetime


class TimeTest(unittest.TestCase):
    def test_year(self):
        now = datetime.now()
        self.assertEqual(2017, now.year)

    def test_timestamp(self):
        now = datetime.utcnow()
        # 取个时间戳真心塞，这么多代码
        timestamp = int(calendar.timegm(now.timetuple()) * 1000 + now.microsecond / 1000)
        self.assertGreater(timestamp, 0)

    def test_format(self):
        now = datetime.utcnow()

        self.assertEqual(now.strftime('%Y'), '2017')

    def test_parse(self):

        d = datetime.strptime('2017', '%Y')
        self.assertEqual(d.year, 2017)
