class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        def getLength(head):
            cnt = 0
            while head != None:
                cnt += 1
                head = head.next
            return cnt

        listSize = getLength(head)
        partSize, remainSize = listSize // k, listSize % k
        ans = []
        while head != None:
            curPartSize = partSize
            if remainSize > 0:
                remainSize -= 1
                curPartSize += 1

            ans.append(head)
            for _ in range(curPartSize - 1):  # Skip curPartSize-1 times
                head = head.next

            if head == None: break
            head.next, head = None, head.next  # Split the current part, and go next

        while len(ans) < k: ans.append(None)  # Fill to get enough k parts
        return ans