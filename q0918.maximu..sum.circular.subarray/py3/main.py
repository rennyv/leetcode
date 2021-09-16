class Solution:
    def maxSubarraySumCircular(self, nums) -> int:
        max_dp, min_dp = nums[:], nums[:]
        for i in range(1, len(nums)):
            max_dp[i] = (max_dp[i-1] if max_dp[i-1] > 0 else 0) + nums[i]
            min_dp[i] = (min_dp[i-1] if min_dp[i-1] < 0 else 0) + nums[i]
        max_, min_ = max(max_dp), min(min_dp)
        S = sum(nums)

        return max(max_, S-min_) if S!=min_ else max_

def test_ex1():
    sol = Solution()
    nums = [1,-2,3,-2]
    ans = 3

    assert ans == sol.maxSubarraySumCircular(nums)

def test_ex2():
    sol = Solution()
    nums = [5,-3,5]
    ans = 10

    assert ans == sol.maxSubarraySumCircular(nums)

def test_ex3():
    sol = Solution()
    nums = [3,-1,2,-1]
    ans = 4

    assert ans == sol.maxSubarraySumCircular(nums)

def test_ex4():
    sol = Solution()
    nums = [3,-2,2,-3]
    ans = 3

    assert ans == sol.maxSubarraySumCircular(nums)

def test_ex5():
    sol = Solution()
    nums =  [-2,-3,-1]
    ans = -1

    assert ans == sol.maxSubarraySumCircular(nums)

test_ex1()
