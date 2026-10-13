# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root: Optional[TreeNode], max_val: int) -> int:
        if not root: return 0

        count = 0

        if root.val >= max_val:
            count = 1
        
        max_val = max(max_val, root.val)
        count += self.dfs(root.left, max_val)
        count += self.dfs(root.right, max_val)

        return count
    
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)