import unittest
from utils import TreeNode, print_tree

# class TreeNode(object):
#     def __init__(self, val):
#         self.val = val
#         self.left = None

def my_function(root, arg=None):
    return []

class CustomTest(unittest.TestCase):
    a = TreeNode("a")
    b = TreeNode("b")
    c = TreeNode("c")
    d = TreeNode("d")
    e = TreeNode("e")
    f = TreeNode("f")

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f        
    def test01(self):
        input = []
        print_tree(self.a)
        self.assertEqual( my_function(self.a, arg='e'), input )

if __name__ == '__main__':
    unittest.main()