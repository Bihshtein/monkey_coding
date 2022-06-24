import unittest
import numpy


def func(arr: list):
    import itertools
    count = len(arr) - 1
    expected_sum = sum(arr)/2
    if count ==1:
        return arr[0]==arr[1]
    for i in range(1, count):
        for group in itertools.combinations(arr, i):
            if expected_sum == sum(group):
                diff_list = arr
                [diff_list.remove(it) for it in group]
                if sum(diff_list) == sum(group):
                    return True


    return False
class Tests(unittest.TestCase):

    def test_1(self):
        self.assertTrue(func([1, 5, 11, 5]))
        self.assertFalse(func([1, 3, 5]))
        self.assertTrue(func([1, 1]))
        self.assertTrue(func([1, 1, 2]))