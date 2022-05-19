from utils import TreeNode as Node
from utils import print_tree

def tree_levels(root, level=0, levels={}):
    if root is None:
        return []    

    if level not in levels:
        levels[level] = []

    levels[level].append(root.val)

    tree_levels(root.left, level+1, levels)
    tree_levels(root.right, level+1, levels)

    return levels.values()

import unittest
class CustomTest(unittest.TestCase):
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f

    def test01(self):
        print_tree(self.a)
        ans = list( tree_levels(self.a) ) # ->
        # [
        #   ['a'],
        #   ['b', 'c'],
        #   ['d', 'e', 'f']
        # ]
        self.assertEqual(ans, [['a'],['b', 'c'],['d', 'e', 'f']], "check yo code")
                
if __name__ == '__main__':
    unittest.main()

