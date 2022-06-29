import unittest

def func(text, voc, curr_sentence, sentences):
    if text in voc:
        sentences.append(curr_sentence + ' ' + text)
    else:
        curr_word = ''
        for i in range(len(text)):
            curr_word += text[i]
            if curr_word in voc:
                if curr_sentence != '':
                    new_sentence = curr_sentence + ' ' + curr_word
                else:
                    new_sentence =  curr_word
                func(text[i+1:],voc,new_sentence,  sentences)




class Test(unittest.TestCase):
    def test1(self):
        sentences = []
        func('catsanddog',["cats", "cat", "and", "sand", "dog"],'',sentences)
        self.assertEqual(['cat sand dog', 'cats and dog'], sentences)