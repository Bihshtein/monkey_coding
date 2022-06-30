import unittest

def is_potential_palindrome(text):
    chars = [0 for i in range(26)]
    for char in text:
        chars[ord(char)-96] += 1
    return chars.count(2)*2+1 >= len(text)

def longest_palindrome(text):
    max_len = 0
    count = len(text)
    for i in range(count):
        for j in range(count):
            if i+j>count-1:
                break
            if is_potential_palindrome(text[i:count-j]):
                curr_len = len(text) - i -j
                if curr_len>max_len:
                    max_len = curr_len
    return  max_len

class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(3, longest_palindrome('cabae'))
        self.assertEqual(6, longest_palindrome('adbabd'))