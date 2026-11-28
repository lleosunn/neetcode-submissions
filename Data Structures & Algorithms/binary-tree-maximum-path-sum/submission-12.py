# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global_best = root.val

        def dfs(root):
            nonlocal global_best 
            if not root: return 0
            best_left = max(dfs(root.left), 0)
            best_right = max(dfs(root.right), 0)
            global_best = max(global_best, root.val + best_left + best_right)
            return root.val + max(best_left, best_right)
            
        dfs(root)
        return global_best

