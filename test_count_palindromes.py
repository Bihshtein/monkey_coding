import math
import unittest

def is_actual_palindrome(text):
    if len(text)==1:
        return  True
    for i in range(len(text)):

        if text[i] != text[-(i+1)] and not ((len(text) % 2) == 1 and math.floor(len(text)/2)==i):
            return False
    return True

def longest_palindrome(text):
    all_palindromes = set()
    count = len(text)

    for i in range(count):
        for j in range(count):
            if i+j>count-1:
                break
            if is_actual_palindrome(text[i:count-j]):
                all_palindromes.add(text[i:count-j])
    print(all_palindromes)
    return len(all_palindromes)


class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(5, longest_palindrome('abaaa'))
        self.assertEqual(4, longest_palindrome('geek'))
