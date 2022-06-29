import unittest

def func(arr, k):
    return max(_func(arr,k))

def _func(arr, k):
    arr_sum = sum(arr)
    count = len(arr)

    if k == 1:
        return [arr_sum]

    curr_sum = 0
    for i in range(count -1, 0, -1):
        curr_sum += arr[i]
        if (((arr[i-1])+curr_sum)*k > arr_sum ) and  curr_sum > arr[i-1]:
            return [curr_sum] + _func(arr[:i], k-1)




class Tests(unittest.TestCase):
    def test_i(self):
        self.assertEqual(35, func([5,10,30,20,15], 3))
        self.assertEqual(60, func([10,20,30,40], 2))

