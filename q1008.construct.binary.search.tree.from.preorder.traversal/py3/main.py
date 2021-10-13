# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) <= 0:
            return None
        
        root_val = preorder[0]
        right_start_idx = len(preorder)
        for i, v in enumerate(preorder[1:]):
            if v > root_val:
                right_start_idx = i+1
                break
        
        leftSubTree = self.bstFromPreorder(preorder[1:right_start_idx])
        rightSubTree = self.bstFromPreorder(preorder[right_start_idx:])
        
        return TreeNode(root_val, leftSubTree, rightSubTree)