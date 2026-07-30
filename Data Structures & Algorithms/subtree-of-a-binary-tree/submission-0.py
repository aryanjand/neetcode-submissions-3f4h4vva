# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checkTree(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            if root.val != subRoot.val:
                return False
            return checkTree(root.left, subRoot.left) and checkTree(root.right, subRoot.right)
        
        def isSubTree(root, subRoot):
            if not root:
                return False

            if root.val == subRoot.val:
                res = checkTree(root, subRoot)
                if res:
                    return True

            return isSubTree(root.left, subRoot) or isSubTree(root.right, subRoot)
        
        return isSubTree(root, subRoot)