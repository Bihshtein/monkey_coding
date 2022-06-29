import unittest


def numberOfPainters(arr, maxLen):
    total = 0
    numPainters = 1
    for i in arr:
        total += i
        if total > maxLen:
            total = i
            numPainters += 1

    return numPainters


def partition(arr, k):
    max_element = max(arr)
    sum_arr = sum(arr)
    while max_element < sum_arr:
        mid = max_element + (sum_arr - max_element) // 2
        requiredPainters = numberOfPainters(arr, mid)
        if requiredPainters <= k:
            sum_arr = mid
        else:
            max_element = mid + 1
    return max_element


class Tests(unittest.TestCase):
    def test_i(self):
        self.assertEqual(2, partition([2, 1, 1, 1], 3))
        self.assertEqual(35, partition([5, 10, 30, 20, 15], 3))
        self.assertEqual(1, partition([1, 1, 1, 1], 4))
        self.assertEqual(2, partition([1, 1, 1, 1], 3))
        self.assertEqual(60, partition([10, 20, 30, 40], 2))



