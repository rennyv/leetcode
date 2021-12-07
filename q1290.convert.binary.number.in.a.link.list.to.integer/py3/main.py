# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        def getStr(head) -> str:
            if not head:
                return ""
            return str(head.val) + getStr(head.next)
        return int(getStr(head), 2)

    

