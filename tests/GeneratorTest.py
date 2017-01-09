import unittest


class GeneratorTest(unittest.TestCase):
    def test_generator_comprehension(self):
        numbers = [1, 2, 3, 4]

        gen = (
            x for x in numbers
        )

        self.assertEqual(next(gen), 1)
        self.assertEqual(next(gen), 2)
        self.assertEqual(next(gen), 3)
        self.assertEqual(next(gen), 4)

        # 没有下一个元素的时候就会报错
        with self.assertRaises(StopIteration):
            self.assertEqual(next(gen), None)

    def test_yield(self):
        def a(e=False):
            if e:
                yield 1

        enabled = a(True)
        self.assertEqual(next(enabled), 1)

        with self.assertRaises(Exception):
            disabled = a()
            self.assertEqual(next(disabled), 1)

    def test_simple_yield(self):
        def request():
            yield "{}"

        r = request()

        self.assertEqual(
            next(r),
            "{}"
        )

    def test_iter_generator(self):
        def request():
            yield "{1}"
            yield "{2}"

        r = request()

        self.assertEqual(
            [x for x in r],
            ["{1}", "{2}"]
        )

    def test_generator_send(self):
        def request():
            var = yield 0
            yield var

        r = request()

        self.assertEqual(
            next(r),
            0
        )

        self.assertEqual(
            r.send(1),
            1
        )

    def test_generator_throw(self):
        def request():
            yield 0
            yield 1

        r = request()

        self.assertEqual(
            next(r),
            0
        )

        with self.assertRaises(BaseException):
            r.throw(BaseException)

    def test_generator_close(self):
        def request():
            for x in range(10):
                yield x

        r = request()

        self.assertEqual(next(r), 0)

        self.assertEqual(next(r), 1)

        r.close()

        with self.assertRaises(BaseException):
            next(r)
