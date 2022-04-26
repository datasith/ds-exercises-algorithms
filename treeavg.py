from util import TreeNode

# class TreeNode(object):
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

def dfs(node, data={}, level=0):
    if not node:
        return None

    if level not in data:
        data[level] = []

    data[level].append(node.val)

    dfs(node.left, data, level+1)
    dfs(node.right, data, level+1)

    avg = []
    for l in data:
        avg.append( sum(data[l]) / len(data[l]) ) 

    return avg

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

    print(dfs(a))
'''
   1
 /   \
 2    3
/ \  /
4 5  6
[1,2.5,5]
'''