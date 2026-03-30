# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def DFS(node: Optional[TreeNode]):
            if not node:
                return 0
            
            leftH = DFS(node.left)
            rightH = DFS(node.right)

            return 1 + max(leftH, rightH)

        return DFS(root)
