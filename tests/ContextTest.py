import unittest


class ContextText(unittest.TestCase):
    @staticmethod
    def test_instance():
        class runner(object):
            def __enter__(self):
                pass

            def __exit__(self, exc_type, exc_val, exc_tb):
                if exc_type is None:
                    raise BaseException
                # exit 返回 True 就不会报错了
                return True

        r = runner()

        with r:
            raise Exception
