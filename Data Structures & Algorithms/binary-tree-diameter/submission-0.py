# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def DFS(node) -> int:
            nonlocal res

            if not node:
                return 0
            
            l = DFS(node.left)
            r = DFS(node.right)

            res = max(res, l + r)

            return 1 + max(l, r)
        DFS(root)
        return res