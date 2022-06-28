import unittest


def func(arr: list):
    bigger_counts = [0 for i in range(len(arr))]
    for i in range(len(arr)):
        for j in range(i , len(arr)):
            if arr[i] < arr[j]:
                bigger_counts[i] += 1
    count = 0

    i = 0
    longest_subsequence = []

    while i < len(arr):
        current_subset = bigger_counts[i:]
        max_id = 0
        max_value = 0
        max_found = False
        for j in range(len(arr)-i):
            if current_subset[j] >= max_value and \
                    (len(longest_subsequence)==0 or arr[i+j] > longest_subsequence[len(longest_subsequence) -1]):
                max_value = current_subset[j]
                max_id = j
                max_found = True
        new_index = i + max_id
        i = new_index +1
        if max_found:
            longest_subsequence.append(arr[new_index])
            count += 1

    return  count




class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(3, func([5,8,3,7,9,1]))

        self.assertEqual(6, func([0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]))

