class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

from collections import deque
def invertTree(root):
    if not root:
        return None

    queue = deque( [root] ) 
    output = []
    while queue:
        current = queue.popleft()
        output.append(current.val)
        swap(current)
        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)
    return output


def swap(node):
    node.left, node.right = node.right, node.left

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
