import unittest


class ClassTest(unittest.TestCase):
    def test_str(self):
        self.assertTrue(isinstance('', str))

    def test_create(self):
        class A(object):
            # pass
            pass

        self.assertTrue(isinstance(A(), A))

        class B(object):
            def my_self(self): return self

        b = B()
        self.assertTrue(b == b.my_self())

    def test_init(self):
        class People(object):
            def __init__(self):
                self.name = 'Tom'

        tom = People()
        self.assertEqual(tom.name, 'Tom')

        class Worker(object):
            # 实例化的时候只用传递 self 往后的参数
            def __init__(self, name):
                self.name = name

        lucy = Worker("Lucy")
        self.assertEqual(lucy.name, 'Lucy')

    def test_method(self):
        class Animal(object):
            def __init__(self, name):
                self.name = name

            def greet(self):
                return 'I am ' + self.name

        cat = Animal('cat')
        self.assertEqual(cat.greet(), 'I am cat')

    def test_hidden_property(self):
        class A(object):
            def __init__(self, foo):
                # __xxx__ 是特殊变量，必要用
                self.__foo = foo

            def get_foo(self):
                return self.__foo

        a = A(12)

        with self.assertRaises(AttributeError):
            self.assertEqual(a.__foo, 12)

    def test_class_type(self):
        class A(object):
            pass

        a = A()

        # type() 返回值怎么参与表达式
        self.assertEqual(str(type(a)), "<class 'tests.ClassTest.ClassTest.test_class_type.<locals>.A'>")

        self.assertTrue(isinstance(a, A))

    def test_inheritance(self):
        class A(object):
            def __init__(self):
                self.age = 0

        class B(A):
            def __init__(self):
                self.name = 'b'

            @staticmethod
            def awesome():
                return 'awesome'

        b = B()

        self.assertEqual(b.awesome(), 'awesome')

        with self.assertRaises(AttributeError):
            # 如果 B 重载了构造函数
            self.assertEqual(b.age, 0)

    def test_polymorphic(self):
        class Animal(object):
            pass

        class Dog(Animal):
            @staticmethod
            def greet():
                return 'dog'

            pass

        class Cat(Animal):
            @staticmethod
            def greet():
                return 'cat'

            pass

        cat = Cat()
        dog = Dog()
        animals = (dog, cat)

        self.assertTrue(isinstance(cat, Cat))
        self.assertTrue(isinstance(cat, Animal))

        # which is Cat, Animal, object
        self.assertEqual(len(Cat.mro()), 3)

        # polymorphic
        self.assertEqual(
            list(map(lambda a: a.greet(), animals)),
            ['dog', 'cat']
        )

    def test_class_method(self):
        class Shape(object):
            __area = 0

            @classmethod
            def get_area(self):
                return self.__area

            @staticmethod
            def static_area():
                return 0

            def normal_method(self):
                return self

        class Box(Shape):
            def foo(self):
                return 0

        class Ellipse(Shape):
            def foo(self):
                return 0

        class RoundShape(object):
            @staticmethod
            def zero():
                return 0

        self.assertEqual(Shape.get_area(), 0)
        self.assertEqual(RoundShape.zero(), 0)

        box = Box()
        ellipse = Ellipse()

        # different class method
        self.assertNotEqual(box.foo, ellipse.foo)
        # same class method but bound different instance
        self.assertNotEqual(box.get_area, ellipse.get_area)
        # exact the same method
        self.assertEqual(box.static_area, ellipse.static_area)
