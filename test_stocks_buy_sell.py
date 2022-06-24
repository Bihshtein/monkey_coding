import unittest


def func(prices):
    prices_count = len(prices) -1
    i = 0
    if prices_count == 1:
        return None
    res = []
    while i < prices_count:
        while i < prices_count and prices[i] >= prices[i+1]:
            i += 1
        buy = i
        i += 1
        if i == prices:
            break
        while i < prices_count and prices[i] <= prices[i + 1]:
            i += 1
        sell = i

        res.append((buy, sell))

    return res


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual([(0, 3), (4, 6)], func([100, 180, 260, 310, 40, 535, 695]))
        self.assertEqual([(0, 4), (5, 7)], func([100, 180, 260, 310,310, 40, 535, 695]))
        self.assertEqual([(0, 4), (5, 7), (8,10)], func([100, 180, 260, 310, 310, 40, 535, 695, 10, 20 , 700]))
