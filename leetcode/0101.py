import sys
sys.path.insert(0, '..')
from utils import TreeNode, print_tree

# class TreeNode(object):
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

def is_symmetric(root):
    if not root:
        return True
    
    if _is_symmetric(root, root) == False:
        return False

    return True

def _is_symmetric(left, right):
    if left == None and right == None:
        return True

    if left == None or right == None:
        return False

    if left.val != right.val:
        return False

    return _is_symmetric(left.left, right.right) and _is_symmetric(left.right, right.left)

import unittest
class CustomTest(unittest.TestCase):
    def test01(self):
        a = TreeNode(1)
        b = TreeNode(2)
        c = TreeNode(2)
        d = TreeNode(3)
        e = TreeNode(3)

        a.left = b
        a.right = c
        b.left = d
        c.right = e        
        print_tree(a)
        self.assertEqual( is_symmetric(a), True )

    def test02(self):
        a = TreeNode(1)
        b = TreeNode(2)
        c = TreeNode(2)
        d = TreeNode(3)
        e = TreeNode(4)

        a.left = b
        a.right = c
        b.left = d
        c.right = e        
        print_tree(a)
        self.assertEqual( is_symmetric(a), False )        

if __name__ == '__main__':
    unittest.main()