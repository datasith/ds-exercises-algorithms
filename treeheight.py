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
    root_2 = TreeNode(10)
    root_2.left = TreeNode(8)
    root_2.right = TreeNode(15)
    root_2.left.left = TreeNode(4)
    root_2.left.left.right = TreeNode(5)
    root_2.left.left.right.right = TreeNode(6)
    root_2.right.left =TreeNode(14)
    root_2.right.right = TreeNode(16)
    print(treeheight(root_2))