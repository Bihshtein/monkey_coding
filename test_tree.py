import unittest


class Node:
    def __init__(self, val:object, left,right):
        self.val = val
        self.left = left
        self.right = right


class Tests(unittest.TestCase):
    def test1(self):
        tree = Node(val=3, left=Node(1,Node(2,None,None),None), right=Node(2,None,None))
        self.assertEqual(8, func(tree))
def func(tree):
    if tree ==None :
        return 0
    else:
        return tree.val + func(tree.left)+ func(tree.right)


