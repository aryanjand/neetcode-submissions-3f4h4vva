# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def cloneAndInvert(node):
            if not node:
                return
            res = TreeNode(node.val) 
            res.left = cloneAndInvert(node.right)
            res.right = cloneAndInvert(node.left)
            return res

        return cloneAndInvert(root)