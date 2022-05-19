from utils import TreeNode as Node, print_tree

def leaf_list(root, output=[]):
    if root is None:
        return []

    if root.left is None and root.right is None:
        output.append(root.val)

    leaf_list(root.left, output)
    leaf_list(root.right, output)

    return output

import unittest

class CustomTest(unittest.TestCase):
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    print_tree(a)
    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f
    def test01(self):
        ans = leaf_list(self.a) # -> [ 'd', 'e', 'f' ]
        self.assertEqual(ans, [ 'd', 'e', 'f' ])

if __name__ == '__main__':
    unittest.main()

