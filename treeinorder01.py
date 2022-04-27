from utils import TreeNode, print_tree

# class TreeNode(object):
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

def inorder(root, output=[]):
    if not root:
        return []

    inorder(root.left)
    output.append(root.val)
    inorder(root.right)
    return output

if __name__ == '__main__':
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

    a.left = b
    a.right = c

    ans = inorder(a)
    assert ans == [1, 5, 1, 8, 7, 1, 7, 1], "check yo code" 
    print_tree(a)
    print(ans)