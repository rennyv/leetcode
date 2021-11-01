"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head == None:
            return None

        stack = [head]
        pNode = None

        while len(stack) > 0:
            cNode = stack.pop()
            if cNode.next:
                stack.append(cNode.next)
            if cNode.child:
                stack.append(cNode.child)

            if pNode:
                pNode.next = cNode
                cNode.prev = pNode
            
            cNode.child = None
            pNode = cNode
        
        return head
