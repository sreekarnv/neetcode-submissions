# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res: int = 0

    def dfs(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        self.res = max(self.res, abs(right - left))

        return 1 + max(left, right)


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.dfs(root)

        return self.res <= 1