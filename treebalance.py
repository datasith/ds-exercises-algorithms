from utils import TreeNode, print_tree

# class TreeNode(object):
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

def is_balanced(root):
    if not root:
        return True
    
    if abs( height(root.left) - height(root.right) ) > 1:
        return False
    
    return is_balanced(root.left) and is_balanced(root.right)
    
def height(root):
    if not root:
        return -1
        
    return 1+max(height(root.left), height(root.right))

if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)

    a.left = b
    a.right = c

    ans = is_balanced(a)
    assert ans == True, "check yo code" 
    print_tree(a)
    print(ans)