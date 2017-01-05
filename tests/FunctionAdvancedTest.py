import unittest
from functools import wraps, partial


class FunctionAdvancedTest(unittest.TestCase):
    def test_higher_order(self):
        def double(i): return i * 2

        def triple(i): return i * 3

        def apply_method_to_number(method, number): return method(number)

        self.assertEqual(apply_method_to_number(double, 1), 2)
        self.assertEqual(apply_method_to_number(triple, 1), 3)

    def test_list_comprehension(self):
        result = [x for x in range(10)]
        self.assertEqual(len(result), 10)
        odd = [x for x in range(10) if x % 2 == 0]
        self.assertEqual(len(odd), 5)

    def test_map(self):
        a = 'hello world'.split()
        self.assertEqual(
            list(map(str.upper, a)),
            ['HELLO', 'WORLD']
        )

    def test_map_lazy(self):
        a = 'hello world'.split()

        # 这个地方可不加括号么？
        def upper(e): raise RuntimeError

        m = map(upper, a)

        with self.assertRaises(RuntimeError):
            # 迭代器只有在取值的时候才会运行 mapper function
            list(m)

    def test_reduce(self):
        a = [1, 2, 3, 4, 5]
        with self.assertRaises(NameError):
            # reduce is moved to functools for readability
            reduce(
                lambda a, b: a + b,
                a,
                0
            )

    def test_filter(self):
        a = [1, 2, 3, 4, 5]

        even = filter(
            lambda a: a % 2 == 1,
            a
        )

        self.assertEqual(list(even), [1, 3, 5])

    def test_lambda(self):
        self.assertTrue(
            (lambda x: x)(True)
        )

        self.assertEqual(str(type(lambda a: a)), "<class 'function'>")

    def test_closure(self):
        def counter():
            base = 0

            def execute():
                # https://segmentfault.com/a/1190000004461404
                # http://newoxygen.github.io/post/python%EF%BC%9Anonlocal%E5%92%8Cglobal%E5%87%BD%E6%95%B0%E6%8E%A2%E7%A9%B6/
                nonlocal base
                base += 1
                return base

            return execute

        c = counter()
        self.assertEqual(c(), 1)
        self.assertEqual(c(), 2)

    def test_decorator_original(self):
        def span(text):
            return '<span>' + text + '</span>'

        def a(func):
            def wrapped(text):
                return '<a>' + func(text) + '</a>'

            return wrapped

        enhanced = a(span)

        self.assertEqual(enhanced('z'), '<a><span>z</span></a>')

    def test_decorator(self):
        def a(original_func):
            if callable(original_func):
                #  消除装饰器的副作用
                #  https://funhacks.net/explore-python/Functional/decorator.html
                @wraps(original_func)
                def wrapped(*args, **kargs):
                    # 把原来的参数原封不动的给原始函数
                    return '<a>' + original_func(*args, **kargs) + '</a>'

                return wrapped
            else:
                def decorate(func):
                    @wraps(func)
                    def wrapped(*args, **kargs):
                        # 把原来的参数原封不动的给原始函数
                        return '<a href="' + original_func + '">' + func(*args, **kargs) + '</a>'

                    return wrapped

                return decorate

        @a
        def span1(text):
            return '<span>' + text + '</span>'

        self.assertEqual(span1('z'), '<a><span>z</span></a>')

        @a('#')
        def span2(text):
            return '<span>' + text + '</span>'

        self.assertEqual(span2('z'), '<a href="#"><span>z</span></a>')

        self.assertEqual(span2.__name__, 'span2')

    def test_partial(self):
        def sub(x, y):
            return x - y

        def customizedPartial(func, *args, **kwargs):
            def wrapped(*real_args, **real_kwargs):
                return func(args,**kwargs)

        minus1 = lambda y: sub(0, y)
        self.assertEqual(minus1(1), -1)

        minus2 = partial(sub, 0)
        self.assertEqual(minus2(1), -1)
