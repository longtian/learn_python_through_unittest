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

    def test_yeild(self):
        def a(enabled=False):
            print('cont')
            if enabled:
                yield 1

        enabled = a(True)
        self.assertEqual(next(enabled), 1)

        disabled = a()
        self.assertEqual(next(disabled), 1)
