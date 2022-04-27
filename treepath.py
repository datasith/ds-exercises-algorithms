import unittest
from utils import TreeNode, print_tree

# class TreeNode(object):
#     def __init__(self, val):
#         self.val = val
#         self.left = None

def path_finder(root, target):
  if not root:
    return
  
  if root.val == target:
    return [ root.val ]
  
  left = path_finder(root.left, target)
  if left:
    return [root.val, *left]
  
  right = path_finder(root.right, target)
  if right:
    return [root.val, *right]  
  
  return None

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
        print_tree(self.a)
        self.assertEqual( path_finder(self.a, 'e'), [ 'a', 'b', 'e' ] )

if __name__ == '__main__':
    unittest.main()