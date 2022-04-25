class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def post_order(root):
  # preorder
  stack = [ root ]
  output = []
  
  while stack:
    current = stack.pop()
    output.append(current.val)
    
    if current.right:
      stack.append(current.right)
    
    if current.left:
      stack.append(current.left)
      
  return output

  # inorder
  stack = []
  output = []
  current = root
  
  while stack or current:
    if current:
      stack.append(current)      
      current = current.left
    else:
      current = stack.pop()
      output.append(current.val)
      current = current.right
  return output

  stack = []
  output = []
  current = root
 
  while stack or current:
    if current:
      stack.append(current)
      output.append(current.val)      
      current = current.right
    else:
      current = stack.pop()
      current = current.left
  return output[::-1] 

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
  
#      a
#    /    \
#   b      c
#  / \    / \
# d   e  f   g

print( post_order(a) )
# [ 'd', 'e', 'b', 'f', 'g', 'c', 'a' ] 