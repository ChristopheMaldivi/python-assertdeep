import unittest
from deepdiff import DeepDiff

class Secret:
    def __init__(self, secret: str):
        self.secret = secret

class Pizza:
    def __init__(self, cheese, tomato, mushrooms, secret):
        self.cheese = cheese
        self.tomato = tomato
        self.mushrooms = mushrooms
        self.secret = secret


class PyDiffExampleTestCase(unittest.TestCase):

    def test_can_compare_equal_dict(self):
        t1 = {1:1, 2:2, 3:3, 4:{"a":"hello", "b":[1, 2, 3]}}
        t2 = {1:1, 2:2, 3:3, 4:{"a":"hello", "b":[1, 2, 3]}}
        assertDeepEqual(self, t1, t2)

    def test_can_compare_distinct_dict(self):
        t1 = {1:1, 2:2, 3:3, 4:{"a":"hello world", "b":[1, 2, 3]}}
        t2 = {1:1, 2:2, 3:3, 4:{"a":"hello", "b":[1, 2, 3]}}
        assertDeepNotEqual(self, t1, t2)

    def test_can_compare_equal_Pizza(self):
        pizza1 = Pizza(True, True, True, Secret("apple"))
        pizza2 = Pizza(True, True, True, Secret("apple"))
        assertDeepEqual(self, pizza1, pizza2)

    def test_can_compare_distinct_Pizza(self):
        pizza1 = Pizza(True, True, True, Secret("apple"))
        pizza2 = Pizza(True, True, True, Secret("ananas"))
        assertDeepNotEqual(self, pizza1, pizza2)

def assertDeepEqual(zelf, o1, o2):
    o1Dict = getattr(o1, '__dict__', None)
    o2Dict = getattr(o2, '__dict__', None)
    if (o1Dict is not None and o2Dict is not None):
        ddiff = DeepDiff(o1.__dict__, o2.__dict__)
    else:
        ddiff = DeepDiff(o1, o2)
    zelf.assertEqual(ddiff, {})

def assertDeepNotEqual(zelf, o1, o2):
    o1Dict = getattr(o1, '__dict__', None)
    o2Dict = getattr(o2, '__dict__', None)
    if (o1Dict is not None and o2Dict is not None):
        ddiff = DeepDiff(o1.__dict__, o2.__dict__)
    else:
        ddiff = DeepDiff(o1, o2)
    zelf.assertNotEqual(ddiff, {})

if __name__ == '__main__':
        unittest.main()
