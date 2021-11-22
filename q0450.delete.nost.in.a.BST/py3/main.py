# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root:
            diff = key - root.val
            if diff < 0:
                root.left = self.deleteNode(root.left, key)
            elif diff > 0:
                root.right = self.deleteNode(root.right, key)
            else:
                if not (root.left or root.right):
                    root = None
                elif not root.left:
                    root = root.right
                elif not root.right:
                    root = root.left
                else:
                    tmp = root.left
                    while tmp.right:
                        tmp = tmp.right
                    root.val = tmp.val
                    root.left = self.deleteNode(root.left, root.val)
        return root
