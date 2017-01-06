import unittest
from collections import Iterable


class IteratorTest(unittest.TestCase):
    def test_next(self):
        class A(object):
            def __init__(self):
                self.count = 1

            # 必须有
            def __iter__(self):
                return self

            def __next__(self):
                self.count -= 1
                if self.count < 0:
                    self.count = 1;
                    raise StopIteration

                return self.count

        a = A()
        self.assertIsInstance(a, Iterable)

        data = [i for i in a]

        # 第二次怎么重置?
        data2 = [i for i in a]

        self.assertEqual(data, [0])
        self.assertEqual(data2, [0])

    def test_my_map(self):

        def my_map(func, target):
            if not isinstance(target, Iterable):
                raise TypeError

            i = iter(target)
            res = []

            while True:
                try:
                    n = next(i)
                    res.append(func(n))
                except StopIteration:
                    return res

        numbers = [1, 2, 3]
        result = my_map(lambda a: a * 2, numbers)
        self.assertEqual(result, [2, 4, 6])

    def test_delayed_map(self):
        class DIter(object):
            def __init__(self, func, it):
                self.func = func;
                self.it = it

            def __iter__(self):
                return self

            def __next__(self):
                return self.func(next(self.it))

        def d_map(func, target):
            return DIter(func, iter(target))

        numbers = [1, 2, 3]
        dm = d_map(lambda a: a * 2, numbers)

        self.assertEqual(list(dm), [2, 4, 6])
