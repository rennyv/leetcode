

from sys import maxsize


class Solution:
    def maxProfit(self, prices):
    # buy&sell stock many transactions with 1 day cooldown: keep track of 3 states; when you do nothing, when you sell, when you buy
    # prices:     1  2  3  0 1
    # do_nothing: 0  1  1  2 2
    # sold:       1  1  2 -1 2
    # holding:   -1 -1 -1  1 1
    # do_nothing = max(do_nothing, sold)
    # sold = holding + price
    # holding = max(holding, do_nothing-price)
        do_nothing = 0
        holding = -maxsize-1
        sold = 0
        
        for price in prices:
            prev_do_nothing = do_nothing
            do_nothing = max(do_nothing, sold)
            sold = holding + price
            holding = max(holding, prev_do_nothing - price)
        
        return max(sold, do_nothing)

def test_ex1():
    prices = [1,2,3,0,2]
    ans = 3

    sol = Solution()
    assert ans == sol.maxProfit(prices)

def test_ex2():
    prices = [1]
    ans = 0

    sol = Solution()
    assert ans == sol.maxProfit(prices)

test_ex1()