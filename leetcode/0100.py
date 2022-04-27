import sys
sys.path.insert(0, '..')
from utils import TreeNode, print_tree

# class TreeNode(object):
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

def is_same_tree(root1, root2):
    if not root1 and not root2:
        return True

    if not root1 or not root2:
        return False

    if root1.val != root2.val:
        return False

    if is_same_tree(root1.left, root2.left) and is_same_tree(root1.right, root2.right):
        return True

    return False
    
import unittest
class CustomTest(unittest.TestCase):
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(2)
    d = TreeNode(3)
    e = TreeNode(3)

    a.left = b
    a.right = c
    b.left = d
    c.right = e  

    f = TreeNode(1)
    g = TreeNode(2)
    h = TreeNode(2)
    i = TreeNode(3)
    j = TreeNode(4)

    f.left = g
    f.right = h
    g.left = i
    h.right = j
    print_tree(f)    
    def test01(self):              
        print_tree(self.a)
        self.assertEqual( is_same_tree(self.a, self.a), True )

    def test02(self):
        print_tree(self.f)
        self.assertEqual( is_same_tree(self.a, self.f), False )

if __name__ == '__main__':
    unittest.main()