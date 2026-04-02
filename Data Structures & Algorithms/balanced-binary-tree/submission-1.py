# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        res = 0
        def DFS(node) -> int:
            nonlocal res
            if not node:
                return 0
            
            l = 1 + DFS(node.left)
            r = 1 + DFS(node.right)

            if 1 < abs(l - r):
                return math.inf

            return max(res, l, r)
        
        l = DFS(root.left)
        r = DFS(root.right)

        return 1 >= abs(l - r)