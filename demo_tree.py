class TreeNode:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.v:
            if node.l is not None:
                self._add(val, node.l)
            else:
                node.l = TreeNode(val)
        else:
            if node.r is not None:
                self._add(val, node.r)
            else:
                node.r = TreeNode(val)

    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if val == node.v:
            return node
        elif (val < node.v and node.l is not None):
            return self._find(val, node.l)
        elif (val > node.v and node.r is not None):
            return self._find(val, node.r)

    def deleteTree(self):
        # garbage collector will do this for us. 
        self.root = None

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.l)
            print(str(node.v) + ' ')
            self._printTree(node.r)
    
if __name__ == '__main__':
    '''
    Tree sctructure
         10  
      /      \
    None    None
    '''
    root = TreeNode(10)
    root.left = TreeNode(34)
    root.right = TreeNode(50)
    '''
    Tree sctructure
           10  
        /      \
      34       50
    /    \     /    \
    None  None None  None
    '''
    root.printTree()