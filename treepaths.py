class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def treepaths(root, treepath = [], paths=[]):
    if not root:
        return

    if not root.left and not root.right:
        treepath.append(root.val)
        paths.append(treepath)
    
    if root.left:
        left = [ *treepath ]
        left.append(root.val)
        treepaths(root.left, left, paths)

    if root.right:
        right = [ *treepath ]
        right.append(root.val)
        treepaths(root.right, right, paths)

    return paths

if __name__ == "__main__":
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)

    a.left = b
    a.right = c
    b.right = d
    print(treepaths(a))