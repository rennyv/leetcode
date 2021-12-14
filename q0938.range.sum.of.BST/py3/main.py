# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, TreeNode

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        if root.val >= low and root.val <= high:
            return self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high) + root.val
        elif root.val > high:
            return self.rangeSumBST(root.left, low, high)
        else:
            return self.rangeSumBST(root.right, low, high)