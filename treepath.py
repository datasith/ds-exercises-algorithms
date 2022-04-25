class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def path_finder(root, target):
  if not root:
    return
  
  if root.val == target:
    return [ root.val ]
  
  left = path_finder(root.left, target)
  if left:
    return [root.val, *left]
  
  right = path_finder(root.right, target)
  if right:
    return [root.val, *right]  
  
  return None


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

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

print( path_finder(a, 'e') )# -> [ 'a', 'b', 'e' ]