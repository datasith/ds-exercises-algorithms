class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

from collections import deque
def invertTree(root, output=[]):
    if not root:
        return None
    output.append(root.val)
    root.left, root.right = root.right, root.left
    if root.left:
        invertTree(root.left, output)
    if root.right:
        invertTree(root.right, output)
    return output

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

    print(invertTree(a))
'''
   1
 /   \
 2    3
/ \  /
4 5  6
[1,3,2,6,5,4]
'''
