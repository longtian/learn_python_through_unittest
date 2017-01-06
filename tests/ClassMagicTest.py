import unittest
from unittest.mock import Mock


class ClassMagicTest(unittest.TestCase):
    def test_new(self):
        class A(object):
            def __new__(cls, *args, **kwargs):
                # 重载 __new__ 必须返回
                return object.__new__(cls, *args, **kwargs)

            def __init__(self):
                self.foo = 0

        a = A()
        self.assertEqual(a.foo, 0)

    def test_toString(self):
        class A(object):
            def __str__(self):
                return 'a instance'

        a = A()
        self.assertEqual(str(a), 'a instance')

    def test_iter(self):
        class Range(object):
            def __init__(self, count):
                self.count = count

            def __iter__(self):
                return self

            def __next__(self):
                if self.count == 0:
                    raise StopIteration
                self.count -= 1
                return self.count

        r = Range(3)
        m = Mock()
        for a in r:
            m(a)

        self.assertEqual(m.call_count, 3)

    def test_items(self):

        class A(object):
            ok = 'foo'

            def __getitem__(self, item):
                return item.upper()

        a = A()
        self.assertEqual(a["ok"], 'OK')

        class B(object):
            def __init__(self):
                self.foo = 1

            def __getattr__(self, item):
                return item

        b = B()
        self.assertEqual(b.z, 'z')
        self.assertEqual(b.foo, 1)

    def test_call(self):

        class A(object):
            pass

        class B(A):
            def __call__(self, *args, **kwargs):
                return 0

        b = B()
        self.assertTrue(callable(b))

    def test_property(self):
        class Exam(object):
            def __init__(self, score):
                self.__score = score

            @property
            def score(self):
                return self.__score

            # 为什么这个名字要和 score 一样呢 ？
            @score.setter
            def score(self, val):
                self.__score = val

        e = Exam(99)

        self.assertEqual(e.score, 99)

        e.score = 8
        self.assertEqual(e.score, 8)

    def test_super(self):

        class Animal(object):
            def __init__(self, name):
                self.name = name

        class Cat(Animal):
            def __init__(self, name, age):
                super().__init__(name)
                self.age = age

            @property
            def super(self):
                return super()

        c = Cat('Lulu', 3)

        self.assertEqual(c.name, 'Lulu')
        self.assertEqual(c.age, 3)
