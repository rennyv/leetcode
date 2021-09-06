# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        temp = None
        while head and head.next is not None :
            temp = head.next
            head.next = head.next.next
            temp.next=prev
            prev= temp
        return prev