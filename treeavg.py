class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

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

    a.left = b
    a.right = c

    print( dfs(a) ) 
    