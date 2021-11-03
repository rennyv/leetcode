# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        result = []
        
        def dfs(root, sum):
            sum += root.val
            if root.left is None and root.right is None:
                result.append(sum)
            
            if root.left: dfs(root.left, sum*10)
            if root.right: dfs(root.right, sum*10)
        
        dfs(root, 0)
        return sum(result)