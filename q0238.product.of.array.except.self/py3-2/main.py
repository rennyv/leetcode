from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #have a right product an left product, add current space after
        L = len(nums)
        ans = [1] * L
        r = l = 1

        for i in range(L):
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