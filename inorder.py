class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root, output=[]):
    if not root:
        return

    inorder(root.left, output)
    output.append(root.val)
    inorder(root.right, output)

    return output

if __name__ == "__main__":
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(5)

    a.left = b
    a.right = c
    c.left = d

    print(inorder(a))