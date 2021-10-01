from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
        return dp[amount]

def test_ex1():
    amount = 5
    coins = [1,2,5]

    # Explanation: there are four ways to make up the amount:
    # 5=5
    # 5=2+2+1
    # 5=2+1+1+1
    # 5=1+1+1+1+1
    ans = 4

    sol = Solution()
    assert ans == sol.change(amount, coins)
