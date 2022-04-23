class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def treeheight(root):
    if not root:
        return -1

    return 1 + max(treeheight(root.left),treeheight(root.right))

if __name__ == "__main__":
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)

    a.left = b
    a.right = c
    b.right = d
    print(treeheight(a))