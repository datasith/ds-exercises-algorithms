from utils import TreeNode, print_tree

# class TreeNode(object):
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

def tree_width(root, level=0, levels={}):
  if level not in levels:
    levels[level] = []
  
  if root is not None:
    levels[level].append(root.val)
  else:
    levels[level].append(None)
    return
    
  if root.left == None and root.right == None:
    return   
  
  tree_width(root.left, level+1, levels)
  tree_width(root.right, level+1, levels)
  
  width = 0
  for val_list in levels.values():
    width = max(width, len(val_list))
  # print([ len(l) for l in levels.values() ])  
  return max( [ len(l) for l in levels.values() ] )


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
        ans = tree_width(self.a)
        print(ans)
        self.assertEqual(ans, 4)

if __name__ == '__main__':
    unittest.main()
