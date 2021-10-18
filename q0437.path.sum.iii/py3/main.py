# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        def countSum(root, flag ,targetSum):
            if root is None: return 0

            if root.val == targetSum:
                self.count += 1
            if flag:    
                countSum(root.left,True, targetSum - root.val)
                countSum(root.right, True, targetSum- root.val)
            else:
                countSum(root.left,False, targetSum )
                countSum(root.right, False, targetSum)
                countSum(root.left,True, targetSum - root.val)
                countSum(root.right, True, targetSum - root.val)
            
        countSum(root,False,targetSum)
        return self.count