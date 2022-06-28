import unittest


def func(arr:list):
    n = len(arr)
    sum = 0
    indexes_to_fill = []
    max_height = arr[0]
    for i in range(1,n-1):
        if arr[i] < max_height:
            indexes_to_fill.append(i)
        elif (arr[i] > max(arr) or arr[i] >= max_height) and arr[i] > arr[i+1]:
            for index in indexes_to_fill:
                fill_height = min(max_height, arr[i])
                if arr[index] < fill_height:
                    sum += fill_height - arr[index]
            max_height = arr[i]
            indexes_to_fill.clear()

    for index in indexes_to_fill:
        fill_height = min(max_height, max(arr[n-1], arr[n-2]))
        if arr[index] < fill_height:
            sum += fill_height - arr[index]
    return  sum


class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(6, func([0,1,0,2,1,0,1,3,2,1,2,1]))
        self.assertEqual(10, func([3,0,0,2,0,4]))
        self.assertEqual(10, func([7,4,0,9]))
