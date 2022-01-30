
from typing import List

class Solution:
    def maxProfit(self,  prices: List[int]) -> int:
        min_p = prices[0]
        profit = 0

        for p in prices[1:]:
            profit = max(p - min_p, profit)
            min_p = min(min_p, p)
        
        return profit

def test_ex1():
    prices = [7,1,5,3,6,4]
    ans = 5
    
    sol = Solution()
    assert ans == sol.maxProfit(prices)

def test_ex2():
    prices = [7,6,4,3,1]
    ans = 0
    
    sol = Solution()
    assert ans == sol.maxProfit(prices)

