from utils import TreeNode, print_tree

# class TreeNode(object):
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

def treeheight(root):
    if not root:
        return -1

    return 1 + max(treeheight(root.left),treeheight(root.right))

import unittest
class CustomTest(unittest.TestCase):
    a = TreeNode(7)
    b = TreeNode(5)
    c = TreeNode(1)
    d = TreeNode(1)
    e = TreeNode(8)
    f = TreeNode(7)
    g = TreeNode(1)
    h = TreeNode(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h

    #      7
    #    /   \
    #   5     1
    #  / \     \
    # 1   8     7
    #    /       \
    #   1         1
    #
    def test_01(self):
        print_tree(self.a)
        ans = treeheight(self.a)
        print(ans)
        self.assertEqual(ans, 3)

if __name__ == '__main__':
    unittest.main()