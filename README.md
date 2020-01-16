# python-assertdeep
Example to have dict or objects deep equal assertions

```
def test_can_compare_distinct_Pizza(self):
        pizza1 = Pizza(True, True, True, Secret("apple"))
        pizza2 = Pizza(True, True, True, Secret("ananas"))
        assertDeepNotEqual(self, pizza1, pizza2)
```
