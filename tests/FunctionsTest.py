import unittest


class FunctionsTest(unittest.TestCase):
    def test_definition(self):
        def identity(num): return num

        def name(): return 'world'

        def returnnone(): 1 + 1

        self.assertEqual(identity(1), 1)
        self.assertEqual(name(), 'world')
        self.assertEqual(returnnone(), None)

    def test_arguments(self):
        def require_arg0(name): return name

        with self.assertRaises(TypeError):
            require_arg0()

        def with_default_arg0(x=1):
            return x;

        self.assertEqual(with_default_arg0(), 1)

    def test_not_primitive_arg0(self):
        def add_too_list(L=[]):
            L.append("END")
            return L

        self.assertEqual(add_too_list(), ["END"])

        # 第二次调用的时候参数 L 还是存在
        self.assertEqual(add_too_list(), ["END", "END"])

    def test_arguments(self):
        def a(*numbers):
            return numbers

        self.assertEqual(a(1, 2, 3), (1, 2, 3))

        def b(first, *others):
            if first != 'foo':
                raise TypeError
            return others

        self.assertEqual(b('foo', 1, 2, 3), (1, 2, 3))

        with self.assertRaises(TypeError):
            b('bar')

    def test_keyword_arguments(self):
        def a(name='default', **kwargs):
            if name != 'default':
                raise TypeError
            return kwargs

        self.assertEqual(a(age=12, name='default'), {
            "age": 12
        })

    def test_multiple_arguments_type(self):

        # 必须按照顺序
        def a(x, y=0, *others, **kwargs):
            return {
                "x": x,
                "y": y,
                "others": others,
                "kwargs": kwargs
            }

        self.assertEqual(a(1, 2, 4, 5, 6, q=1), {
            "x": 1,
            "y": 2,
            "others": (4, 5, 6),
            "kwargs": {
                "q": 1
            }
        })

        with self.assertRaises(TypeError):
            # 传了多个 y
            self.assertEqual(a(1, 2, 4, 5, 6, q=1, y=12), {
                "x": 1,
                "y": 2,
                "others": (4, 5, 6),
                "kwargs": {
                    "q": 1
                }
            })
