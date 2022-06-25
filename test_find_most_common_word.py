import unittest


def func(sentence):
    words = sentence.split(' ')
    common_words = {}
    max_word_count = 0
    max_word = ''
    for word in words:
        if word in common_words.keys():
            common_words[word] += 1
        else:
            common_words[word] = 1
        if common_words[word] > max_word_count:
            max_word_count = common_words[word]
            max_word = word
    return max_word


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual('1', func('1 2 3, 1 is 4'))
        self.assertEqual('2', func('1 2 3 2 4 3 2'))