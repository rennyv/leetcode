from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        l = r = 1
        for i in range(len(nums)):
            ans[i] *= l
            ans[~i] *= r
            l *= nums[i]
            r *= nums[~i]
        return ans

def test_ex1():
    nums = [1,2,3,4]
    ans = [24,12,8,6]

    sol = Solution()
    assert ans == sol.productExceptSelf(nums)

def test_ex2():
    nums = [-1,1,0,-3,3]
    ans = [0,0,9,0,0]

    sol = Solution()
    assert ans == sol.productExceptSelf(nums)

test_ex1()

