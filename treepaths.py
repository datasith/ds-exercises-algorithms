import unittest
from utils import TreeNode, print_tree

# class TreeNode(object):
#     def __init__(self, val):
#         self.val = val
#         self.left = None

def all_tree_paths(root, treepath = [], paths=[]):
    if not root:
        return

    treepath.append(root.val)
    
    if root.left is None and root.right is None:
        paths.append( treepath )
    
    if root.left:
        left = [ *treepath ]
        all_tree_paths(root.left, left, paths)

    if root.right:
        right = [ *treepath ]
        all_tree_paths(root.right, right, paths)

    return paths

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
        output = [['a', 'b', 'd'], ['a', 'b', 'e'], ['a', 'c', 'f']]
        self.assertEqual( all_tree_paths(self.a), output )

if __name__ == '__main__':
    unittest.main()