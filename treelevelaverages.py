from utils import TreeNode as Node
from utils import print_tree

# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

def level_averages(root, level=0, levels={}):
    if root is None:
        return None

    if level not in levels:
        levels[level] = [0,0] # -> num, sum

    levels[level][0] += 1
    levels[level][1] += root.val

    level_averages(root.left, level+1, levels)
    level_averages(root.right, level+1, levels)

    output = []
    for lev in levels:
        output.append(levels[lev][1]/levels[lev][0])

    return output

import unittest

class CustomTest(unittest.TestCase):
    a = Node(1)
    b = Node(2)
    c = Node(3)
    a.left = b
    a.right = c

    def test01(self):
        print_tree(self.a)
        ans = level_averages(self.a)
        self.assertEqual(ans, [1, 2.5], "check yo code")

if __name__ == '__main__':
    unittest.main()