class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        L = len(cost) + 1
        dp = [0] * L

        for i in range(2,L):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[-1]


def test_ex1():
    sol = Solution()
    cost = [10,15,20]
    Output = 15
    assert Output == sol.minCostClimbingStairs(cost)

def test_ex2():
    sol = Solution()
    cost = [1,100,1,1,1,100,1,1,100,1]
    Output = 6
    assert Output == sol.minCostClimbingStairs(cost)

test_ex2()