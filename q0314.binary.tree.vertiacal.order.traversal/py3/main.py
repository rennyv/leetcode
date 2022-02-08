# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import List, Optional


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append((root, 0))
        col = {}
        
        while q:
            node, c = q.popleft()
            
            if c in col: 
                col[c].append(node.val)
            else:
                col[c] = [node.val]

            if node.left: q.append((node.left, c-1))            
            if node.right: q.append((node.right, c+1))
        
       
        return [col[x] for x in sorted(col.keys())] 



