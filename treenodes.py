import unittest
from util import TreeNode

def count_nodes(node):
    if not node:
        return 0

    return 1 + count_nodes(node.left) + count_nodes(node.right)

class CustomTest(unittest.TestCase):
    def test01(self):
        a = TreeNode(1)
        b = TreeNode(2)
        c = TreeNode(3)
        d = TreeNode(4)
        e = TreeNode(5)
        f = TreeNode(6)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f        
        input = a
        self.assertEqual( count_nodes(a), 6 )

if __name__ == '__main__':
    unittest.main()
    
'''
      1
    /   \
    2    3
   / \  /
  4   5 6

  total nodes: 6
'''