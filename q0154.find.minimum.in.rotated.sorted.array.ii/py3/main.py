from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        while l < r:
            m = (l+r)//2
            if nums[m] > nums[r]: #ans has to be between m+1 and r
                l = m+1
            elif nums[m]==nums[r]: #only case where this would happen is when nums[l] = nums[m] = nums[r], so we decrement and try to re-enter the binary search
                r -= 1
            else:
                r = m #ans has to be between l and m
        return nums[l]
        



def test_ex1():
    nums = [1,3,5]
    ans = 1

    sol = Solution()
    assert ans == sol.findMin(nums)

def test_ex2():
    nums = [2,2,2,0,1]
    ans = 0

    sol = Solution()
    assert ans == sol.findMin(nums)

test_ex2()