class Solution:
    def rob(self, nums) -> int:
        dp = [0, nums[0]]
        for i in range(1,len(nums)):
            dp.append(max(dp[i],nums[i]+dp[i-1]))
        return dp[-1]


def test_ex1():
    nums = [1,2,3,1]
    output = 4
    sol = Solution()
    assert output == sol.rob(nums)

def test_ex2():
    nums = [2,7,9,3,1]
    output = 12
    sol = Solution()
    assert output == sol.rob(nums)

test_ex1()