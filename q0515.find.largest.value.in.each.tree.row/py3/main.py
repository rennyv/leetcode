# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        ans = []
        queue = []
        queue.append( (root,0) )
        
        depthMax = -inf
        depth = 0
        
        while queue:
            node, current_depth = queue.pop(0)

            if depth != current_depth:
                ans.append(depthMax)
                depthMax = -inf
                depth = current_depth
            
            depthMax = max(depthMax, node.val)
            
            if node.left: queue.append((node.left, current_depth+1))
            if node.right: queue.append((node.right, current_depth+1))
        
        ans.append(depthMax)        
        return ans