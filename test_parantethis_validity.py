import unittest


def func(text):
    count = 0
    chars_left = len(text)
    i = 0

    while i < chars_left -1:
        if text[i] == '(' and text[i+1] == ')':
            text = text[:i] + text[i+2:]
            count+=2
            chars_left -=2
        elif text[i] == ')' and i>0 and text[i-1] == '(':
            count += 2
            text = text[:i-1] + text[i+1:]
            chars_left -= 2
            i-=2
        elif text[i] == ')' and i == 0:
            text = text[i+1:]
            chars_left -= 1
        else:
            i = i+1
    return count



class Tests(unittest.TestCase):
    def tests1(self):
        self.assertEqual(6, func('((()))'))
        self.assertEqual(6, func(')((()))('))
        self.assertEqual(4,func(')()())'))
        self.assertEqual(2, func('((()'))

