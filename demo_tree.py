from util import TreeNode, Tree, print_tree

# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#
# class Tree:
#     def __init__(self, root=None):
#         self.root = root

if __name__ == '__main__':
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
    tree = Tree(a) # not tipycally needed — printing is a general function
    print_tree(a)    