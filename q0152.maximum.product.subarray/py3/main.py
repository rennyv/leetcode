class Solution:
    def maxProduct(self, nums):
        max_ = nums[0]
        curMax = curMin = 1
        
        for num in nums:
            if num < 0:
                curMax, curMin = curMin, curMax
            curMax = max(num, curMax*num)
            curMin = min(num, curMin*num)
            max_ = max(curMax, max_)
        return max_

def test_ex1():
    sol = Solution()
    nums = [2,3,-2,4]
    ans = 6
    assert ans == sol.maxProduct(nums)

def test_ex2():
    sol = Solution()
    nums = [-2,0,-1]
    ans = 0
    assert ans == sol.maxProduct(nums)