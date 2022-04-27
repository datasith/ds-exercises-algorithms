import unittest
from utils import TreeNode, print_tree

# class TreeNode(object):
#     def __init__(self, val):
#         self.val = val
#         self.left = None

class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def treesum(root):
    if not root:
        return 0

    return root.val + treesum(root.left) + treesum(root.right)

class CustomTest(unittest.TestCase):
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(5)
    d = TreeNode(6)
    e = TreeNode(10)
    f = TreeNode(12)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f        
    def test01(self):
        print_tree(self.a)
        self.assertEqual( treesum(self.a), 36 )

if __name__ == '__main__':
    unittest.main()