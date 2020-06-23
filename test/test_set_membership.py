import unittest
from more_fun_with_collections import set_membership as sm
a_set = {1, 2, 3, 4, 5}
value_in_set = 3
value_not_in_set = 6


class MyTestCase(unittest.TestCase):
    def test_value_in_set(self):
        self.assertEqual(True, sm.in_set(a_set, value_in_set))

    def test_value_not_in_set(self):
        self.assertEqual(False, sm.in_set(a_set, value_not_in_set))


if __name__ == '__main__':
    unittest.main()
