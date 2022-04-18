class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def treesum(root):
    if not root:
        return float("-inf")
    
    if not root.left and not root.right:
        return root.val

    left = root.val + treesum(root.left)
    right = root.val + treesum(root.right)

    return max(left, right)

if __name__ == "__main__":
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(5)
    e = TreeNode(10)

    a.left = b
    a.right = c
    c.left = d
    b.left = e
    print(treesum(a))