import unittest
from utils import TreeNode, print_tree

# class TreeNode(object):
#     def __init__(self, val):
#         self.val = val
#         self.left = None

def count_nodes(node):
    if not node:
        return 0

    return 1 + count_nodes(node.left) + count_nodes(node.right)

class CustomTest(unittest.TestCase):
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f        
    def test01(self):
        print_tree(self.a)
        self.assertEqual( count_nodes(self.a), 6 )

if __name__ == '__main__':
    unittest.main()