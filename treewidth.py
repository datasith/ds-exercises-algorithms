class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

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
  return levels


if __name__ == "__main__":
  a = TreeNode('a')
  b = TreeNode('b')
  c = TreeNode('c')
  d = TreeNode('d')
  e = TreeNode('e')
  f = TreeNode('f')
  g = TreeNode('g')
  h = TreeNode('h')
  i = TreeNode('i')
  j = TreeNode('j')

  a.left = b
  a.right = c
  b.left = d
  b.right = e
  c.right = f
  e.left = g
  e.right = h
  f.left = i
  d.left = j

  #         a
  #      /    \
  #     b      c
  #   /  \      \
  #  d    e      f
  #      / \    /
  #     g  h   i

  print( tree_width(a) ) # ->
