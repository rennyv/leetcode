# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def dfs(node, parent, depth, value):
            if not node: return None
            
            if node.val == value: return depth, parent
            
            return dfs(node.left, node, depth + 1, value) or dfs(node.right, node, depth + 1, value)
        
        depth_x, parent_x = dfs(root, None, 0, x)
        depth_y, parent_y = dfs(root, None, 0, y)
        
        return depth_x == depth_y and parent_x != parent_y