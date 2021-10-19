from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # could be replaced with List.index(x) but is slower
        lookup = {}
        for i, v in enumerate(nums2):
            lookup[v] = i
        # taking the hit on memory

        ans = []
        for v in nums1:
            ans.append(-1)
            for j in range(lookup[v]+1, len(nums2)):
                if nums2[j] > v:
                    ans[-1] = nums2[j]
                    break;
        return ans




def test_ex1():
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    ans = [-1,3,-1]

    sol = Solution()
    assert ans == sol.nextGreaterElement(nums1, nums2)

def test_ex2():
    nums1 = [2,4]
    nums2 = [1,2,3,4]
    ans = [3,-1]

    sol = Solution()
    assert ans == sol.nextGreaterElement(nums1, nums2)

test_ex1() 