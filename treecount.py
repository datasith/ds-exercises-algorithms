class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def tree_value_count(root, target):
  if not root:
    return 0
  
  return (root.val == target) + tree_value_count(root.right, target) + tree_value_count(root.left, target)  

a = Node(7)
b = Node(5)
c = Node(1)
d = Node(1)
e = Node(8)
f = Node(7)
g = Node(1)
h = Node(1)

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

print(tree_value_count(a,  1)) # -> 4