class Solution:
    def lengthOfLIS(self, nums):
        dp = [0] * len(nums)
        for i in range(len(nums)):
            c = 0
            for j in range(i):
                if nums[i] > nums[j]: c = max(c, dp[j])
            dp[i] = c + 1
        return max(dp)

        
            


def test_ex1():
    nums = [10,9,2,5,3,7,101,18]
    ans = 4

    sol = Solution()
    assert ans == sol.lengthOfLIS(nums)

def test_ex2():
    nums = [0,1,0,3,2,3]
    ans = 4

    sol = Solution()
    assert ans == sol.lengthOfLIS(nums)

def test_ex3():
    nums = [7,7,7,7,7,7]
    ans = 1

    sol = Solution()
    assert ans == sol.lengthOfLIS(nums)

test_ex1()