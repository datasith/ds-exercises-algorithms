class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def treesum(root):
    if not root:
        return 0

    return root.val + treesum(root.left) + treesum(root.right)

if __name__ == "__main__":
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)

    a.left = b
    a.right = c

    print(treesum(a))