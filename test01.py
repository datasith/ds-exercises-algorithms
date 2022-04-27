from utils import TreeNode, print_tree

# class TreeNode(object):
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
        
def all_tree_paths_str(root, paths=[], path = ''):
    if root:
        path += str(root.val)
        
        if not root.left and not root.right:    # if reach a leaf
            paths.append(path)    # update paths    
        else:
            all_tree_paths_str(root.left, paths, path)
            all_tree_paths_str(root.right, paths, path)
    return paths

def all_tree_paths_list(root, paths=[], path = []):
    if root:
        path.append(root.val)
        
        if not root.left and not root.right:    # if reach a leaf
            paths.append(path)    # update paths    
            path = []
        else:
            all_tree_paths_list(root.left, paths, path)
            all_tree_paths_list(root.right, paths, path)
    return paths    

def all_tree_paths(root, paths = [], treepath = []):
    if not root:
            return
        
    if not root.left and not root.right:
            treepath.append(root.val)
            paths.append(treepath)
                
    if root.left:
        treepath_left = [*treepath]
        treepath_left.append(root.val[0])
        all_tree_paths(root.left, paths, treepath_left)

    if root.right:
        treepath_right = [*treepath]
        treepath_right.append(root.val[0])
        all_tree_paths(root.right, paths, treepath_right)
        
    return paths
if __name__ == '__main__':
    a = TreeNode('a')
    b = TreeNode('b')
    c = TreeNode('c')
    d = TreeNode('d')
    e = TreeNode('e')
    f = TreeNode('f')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    print_tree(a)
    print(all_tree_paths_str(a))
    print(all_tree_paths(a))
    print(all_tree_paths_list(a))

