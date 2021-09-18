
class Solution:
    def maxProfit(self, prices) -> int:
        max_diff = 0
        min_day = prices[0]

        for p in prices[1:]:
            if p > min_day:
                max_diff = max(max_diff, p-min_day)
            min_day = min(min_day, p)
        return max_diff


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

test_ex1()