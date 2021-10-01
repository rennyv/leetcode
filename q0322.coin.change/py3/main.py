from typing import List
from sys import maxsize

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [maxsize] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        
        return dp[amount] if dp[amount] != maxsize else -1



def test_ex1():
    coins = [1,2,5]
    amount = 11
    ans = 3
    #Explanation: 11 = 5 + 5 + 1
    sol = Solution()
    assert ans == sol.coinChange(coins, amount)

def test_ex2():
    coins = [2]
    amount = 3
    ans = -1

    sol = Solution()
    assert ans == sol.coinChange(coins, amount)

def test_ex3():
    coins = [1]
    amount = 0
    ans = 0

    sol = Solution()
    assert ans == sol.coinChange(coins, amount)

def  test_ex4():
    coins = [1]
    amount = 1
    ans = 1
        
    sol = Solution()
    assert ans == sol.coinChange(coins, amount)

def test_ex5():
    coins = [1]
    amount = 2
    ans = 2
    
    sol = Solution()
    assert ans == sol.coinChange(coins, amount)