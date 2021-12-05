# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oheader = ListNode()
        eheader = ListNode()
        
        ocursor = oheader
        ecursor = eheader        
        
        while head is not None:
            ocursor.next = head
            ocursor = head
            head = head.next
            
            if head is not None:
                ecursor.next = head
                ecursor = head
                head = head.next
                
        ocursor.next = eheader.next
        ecursor.next = None
                
        return oheader.next
                
            
        