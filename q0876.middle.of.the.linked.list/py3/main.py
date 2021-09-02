# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        midNode=head
        moveNode=head
        move=False
        while not (moveNode is None):
            moveNode = moveNode.next
            if move:
                midNode=midNode.next
            move= not move
        return midNode