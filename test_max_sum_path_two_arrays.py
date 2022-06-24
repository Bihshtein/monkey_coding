import unittest


def func(arr1: list, arr2: list):
    arr1.sort()
    arr2.sort()
    arr1_index = 0
    arr2_index = 0
    arr1_len = len(arr1)
    arr2_len = len(arr2)
    result, sum1, sum2 = 0, 0, 0
    while arr1_index < arr1_len and arr2_index < arr2_len:
        if arr1[arr1_index] < arr2[arr2_index]:
            sum1 += arr1[arr1_index]
            arr1_index += 1

        elif arr1[arr1_index] > arr2[arr2_index]:
            sum2 += arr2[arr2_index]
            arr2_index +=1
        else:
            result += max(sum1,sum2) + arr1[arr1_index]
            arr1_index += 1
            arr2_index += 1
            sum1 = 0
            sum2 = 0

    result += max(sum(arr1[arr1_index:]), sum(arr2[arr2_index:]))
    return result


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(35, func([2,3,7,10,12], [1,5,7,8]))
        self.assertEqual(15, func([1,2,3], [3,4,5]))
        self.assertEqual(15, func([1, 2, 3], [4, 5, 6]))



