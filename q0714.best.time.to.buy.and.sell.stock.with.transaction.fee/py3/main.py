class Solution:
    def maxProfit(self, prices, fee):
        L = len(prices)
        dp = [[-float('inf') for _ in range(2)] for _ in range(L)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0 
        for i in range(1, L):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1] = max(dp[i-1][0] + prices[i] - fee, dp[i-1][1])
            
            
        return max(dp[L-1])


def test_ex1():
    prices = [1,3,2,8,4,9]
    fee = 2
    
    ans = 8
    sol = Solution()
    assert ans == sol.maxProfit(prices, fee)

def test_ex2():
    prices = [1,3,7,5,10,3]
    fee = 3
    
    ans = 6
    sol = Solution()
    assert ans == sol.maxProfit(prices, fee)