import unittest
def change(coin_range, change_amount):
    coin_range.sort()
    options_sets = []
    cleaned_options_set = []

    for coin in coin_range:
        if change_amount in coin_range:
            cleaned_options_set.append((change_amount,))
        if change_amount <= min(coin_range):
            return cleaned_options_set

        options_sets += change(coin_range, change_amount-coin)
        for options_set in options_sets:
            if sum(options_set) + coin == change_amount:
                cleaned_options_set.append(tuple(sorted((coin,) + options_set)))
    return set(cleaned_options_set)

class  Tests(unittest.TestCase):
    def test_1(self):
        print(change([1, 2, 3], 4))

        print(change([5,2,3, 6], 10))
