class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root):
        if not root:
            return True
        
        if abs( height(root.left) - height(root.right) ) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
def height(root):
    if not root:
        return -1
        
    return 1+max(height(root.left), height(root.right))

if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)

    a.left = b
    a.right = c

    sol = Solution()
    ans = sol.isBalanced(a)
    print(ans)