from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        s0 = 0
        h1 = s1 = h2 = s2 = float('-inf')
        for p in prices:
            h1, s1, h2, s2 = max(h1, s0 - p), max(s1, h1 + p), max(h2, s1 - p), max(s2, h2 + p)
        return max(s0, s1, s2)

def test_ex1():
    prices = [3,3,5,0,0,3,1,4]
    ans = 6

    sol = Solution()
    assert ans == sol.maxProfit(prices)

def test_ex2():
    prices = [1,2,3,4,5]
    ans = 4

    sol = Solution()
    assert ans == sol.maxProfit(prices)

def test_ex3():
    prices = [7,6,4,3,1]
    ans = 0

    sol = Solution()
    assert ans == sol.maxProfit(prices)
