import unittest


class SequenceTest(unittest.TestCase):
    def test_chinese(self):
        self.assertEqual(u'你好', u'你好')
        self.assertEqual(len(u'你好'), 2)

    def test_eval(self):
        self.assertEqual(eval('1+1'), 2)

    def test_index(self):
        a = [0, 1, 2]
        self.assertEqual(a[2], 2)
        self.assertEqual(a[-1], 2)

    def test_slice(self):
        a = [0, 1, 2, 3, 4]
        self.assertEqual(a[1:3], [1, 2])
        self.assertEqual(a[3:], [3, 4])
        self.assertEqual(a[-2:], [3, 4])
        self.assertEqual(a[:], a)

    def test_add(self):
        a = [0, 1, 2]
        b = [3, 4, 5]

        self.assertEqual(a + b, [0, 1, 2, 3, 4, 5])

    def test_multiply(self):
        a = [0, 1, 2]

        self.assertEqual(a * 2, [0, 1, 2, 0, 1, 2])

    def test_in(self):
        a = [0, 1, 2]
        self.assertTrue(1 in a)

    def test_list_index(self):
        a = [0, 1, 2, 1]
        self.assertEqual(a.index(1), 1)

    def test_list_count(self):
        a = [0, 0, 1, 1, 2]
        self.assertEqual(a.count(1), 2)

    def test_list_append(self):
        a = list([0, 1, 2])
        a.append(3)
        self.assertEqual(a, [0, 1, 2, 3])

    def test_list_extends(self):
        a = [0, 1, 2]
        b = [3, 4, 5]
        a.extend(b)
        self.assertEqual(a, [0, 1, 2, 3, 4, 5])

    def test_list_insert(self):
        a = [0, 1, 2]
        a.insert(1, 3)
        self.assertEqual(a, [0, 3, 1, 2])

    def test_list_pop(self):
        a = [0, 1, 2]
        poped = a.pop()
        self.assertEqual(poped, 2)
        self.assertEqual(len(a), 2)

    def test_list_popError(self):
        a = []
        try:
            a.pop()
        except IndexError as e:
            self.assertEqual(str(e), "pop from empty list")

    def test_list_remove(self):
        a = [0, 1, 2]
        a.remove(1)
        self.assertEqual(a, [0, 2])

    def test_list_reverse(self):
        a = [0, 1]
        a.reverse()
        self.assertEqual(a, [1, 0])

    def test_list_sort(self):
        a = [0, 2, 1]
        a.sort()
        self.assertEqual(a, [0, 1, 2])

    def test_list_sorted(self):
        a = [0, 2, 1]
        self.assertEqual(sorted(a), [0, 1, 2])

    def test_list_sortedReverse(self):
        a = [0, 2, 1]
        self.assertEqual(sorted(a, reverse=True), [2, 1, 0])

    def test_list_sortedWithKey(self):
        def key(s): return s[1]

        students = [
            ('a', 0),
            ('c', 2),
            ('b', 1)
        ]
        self.assertEqual(
            sorted(students, key=key),
            [
                ('a', 0),
                ('b', 1),
                ('c', 2)
            ]
        )

    def test_tuple_create(self):
        a = (0, 1, 2)
        self.assertEqual(len(a), 3)
        # tuple 和 list 是不等的
        self.assertNotEqual(a, [0, 1, 2])

    def test_tuple_single(self):
        a = ()
        b = (1)
        c = (1,)
        self.assertEqual(len(a), 0)
        self.assertEqual(b, 1)
        self.assertEqual(len(c), 1)

    def test_tuple_append(self):
        a = ()
        with self.assertRaises(AttributeError):
            a.append(1)

    def test_string_methods(self):
        a = 'Apple'
        self.assertEqual(a.find('A'), 0)
        self.assertEqual(a.find('Z'), -1)
        self.assertEqual(a.split('l'), ['App', 'e'])
        self.assertEqual(a.replace('A', 'a'), 'apple')
        self.assertEqual(a.lower(), 'apple')
        self.assertEqual(a.upper(), 'APPLE')
        # 好奇怪为啥有个 ''
        self.assertEqual(a.split('p'), ['A', '', 'le'])

        b = ['0', '1', '2']
        self.assertEqual(''.join(b), '012')

        with self.assertRaises(BaseException):
            c = [0, 1, 2]
            self.assertEqual(''.join(c), '012')

        d = ' _  '
        self.assertEqual(d.strip(), '_')

    def test_dict_create(self):
        d = {}
        self.assertEqual(len(d), 0)
        people = {"name": "Tom"}
        self.assertEqual(people, {"name": "Tom"})
        people["name"] = "Jack"
        self.assertEqual(people["name"], "Jack")
        new_people = dict(name="Jimmy")
        self.assertEqual(new_people, {"name": "Jimmy"})
        people_props = [
            ('name', 'Lucy'),
            ('foo', 1),
            ('foo', 2)
        ]
        self.assertEqual(dict(people_props), {
            "name": "Lucy",
            "foo": 2
        })

    def test_dict_iterate(self):
        d = {
            "foo": 1,
            "bat": 2
        }
        for key in d:
            self.assertTrue(key in d)

        with self.assertRaises(RuntimeError):
            # 遍历对象的时候不能删除
            for key in d:
                del d[key]

        self.assertEqual(str(type(d.keys())), "<class 'dict_keys'>")
        for key in list(d.keys()):
            del d[key]

        self.assertEqual(len(d), 0)

        # 访问不存在的属性会报错
        with self.assertRaises(KeyError):
            print(d["z"])

        # 给不存在的属性赋值不会报错
        d["z"] = 2

    def test_dict_methods(self):
        a = {"name": "Tom"}
        a.clear()
        self.assertEqual(len(a), 0)
        tom = {"age": 20, "country": {"name": "Brazil"}}
        jack = tom.copy()
        self.assertEqual(tom["age"], 20)
        jack["age"] = 12
        jack["country"]["name"] = "Chile"
        self.assertEqual(tom["age"], 20)
        self.assertEqual(tom["country"]["name"], 'Chile')

    def test_dict_get(self):
        a = {"name": "Tom"}
        self.assertEqual(a.get("name"), "Tom")
        self.assertEqual(a.get("age"), None)
        self.assertEqual(a.get("gender", "male"), "male")

    def test_dict_setDefault(self):
        a = {}
        a.setdefault("age", 0)
        self.assertEqual(a.get("age"), 0)
        a["age"] = 18
        self.assertEqual(a.get("age"), 18)

    def test_dict_update(self):
        a = {}
        b = {"country": {"name": "Brazil"}}
        a.update(b)
        self.assertEqual(a, b)
        # to demo update is indeed a shallow copy
        b["country"]["name"] = "Chile"
        self.assertEqual(a, b)

    def test_dict_items(self):
        a = {"name": "Tom"}
        self.assertEqual(str(type(a.items())), "<class 'dict_items'>")
        self.assertEqual(list(a.items())[0], ("name", "Tom"))
        self.assertEqual(len(a.keys()), 1)
        self.assertEqual(list(a.values()), ["Tom"])
        a.popitem()
        self.assertEqual(len(a), 0)

    def test_set_create(self):
        a = {"a", "b"}
        self.assertEqual(len(a), 2)
        a.add("c")
        self.assertEqual(len(a), 3)

        b = set(["1", 1, 1, 1.0, 1.00])
        self.assertEqual(len(b), 2)

    def test_set_operator(self):
        a = {1, 2, 3}
        b = {2, 3, 4}
        c = {2}

        self.assertEqual(a & b, {2, 3})
        self.assertEqual(a | b, {1, 2, 3, 4})
        self.assertEqual(a - b, {1})
        self.assertTrue(c.issubset(a))
        self.assertTrue(a.issuperset(c))
