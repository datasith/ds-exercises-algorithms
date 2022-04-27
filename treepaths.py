import unittest
from utils import TreeNode, print_tree

# class TreeNode(object):
#     def __init__(self, val):
#         self.val = val
#         self.left = None

def treepaths(root, treepath = [], paths=[]):
    if not root:
        return

    if not root.left and not root.right:
        treepath.append(root.val)
        paths.append(treepath)
    
    if root.left:
        left = [ *treepath ]
        left.append(root.val)
        treepaths(root.left, left, paths)

    if root.right:
        right = [ *treepath ]
        right.append(root.val)
        treepaths(root.right, right, paths)

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
        self.assertEqual( treepaths(self.a), output )

if __name__ == '__main__':
    unittest.main()