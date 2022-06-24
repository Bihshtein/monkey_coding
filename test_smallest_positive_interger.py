import unittest


def func(array: list):
    smallest_int = 1
    sum_till_now = 0
    array.sort()
    for item in array:
        if item <= smallest_int:
            sum_till_now += item
            smallest_int = sum_till_now + 1
        else:
            return smallest_int
    return smallest_int


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(2, func([1, 10, 3, 11, 6, 15]))
        self.assertEqual(4, func([1, 1, 1]))
        self.assertEqual(6, func([1, 2, 2]))
        self.assertEqual(7, func([1, 2, 3, 9, 20]))


