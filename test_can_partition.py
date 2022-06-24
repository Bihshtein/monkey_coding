import unittest


def can_partition(n, k, m):
    if len(n) < k:
        return False
    i = k-1
    while i < len(n):
        if n[i] - n[0] > m:
            return False
        if can_partition(n[i+1:], k, m):
            return True
        else:
            i += 1
    return True


def func(n: list, k: int, m: int):
    n.sort()
    return can_partition(n, k, m)


class Tests(unittest.TestCase):
    def test_i(self):
        self.assertTrue(func([8, 3, 9, 1, 2], 2, 3))
        self.assertFalse(func([8, 4, 9, 1, 2], 2, 2))

