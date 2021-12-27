# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next or not head.next.next:
            return head
        
        mid, end = head, head
        
        #find tail and halfway point
        while end.next and end.next.next:
            mid = mid.next
            end = end.next.next
        
        rev_tail, cur = None, mid.next
        mid.next = None
        
        #reverse list
        while cur:
            
            cur.next, rev_tail, cur = rev_tail, cur, cur.next
        
        #merge lists
        cur_head, next_head = head, head.next
        cur_rev_tail, next_rev_tail = rev_tail, rev_tail.next
        
        while True:
            cur_head.next, cur_rev_tail.next = cur_rev_tail, next_head
            
            if next_rev_tail is None:
                return head
            
            cur_head = next_head
            cur_rev_tail = next_rev_tail
            next_head = next_head.next
            next_rev_tail = next_rev_tail.next
            
            