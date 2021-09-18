class Solution:
    def maxProfit(self, prices) -> int:
        total = 0
        yesterday = prices[0]
        buy=0
        hold=False

        for p in prices[1:]:
            if p < yesterday:
                if hold:
                    total+=yesterday-buy
                    hold = False                
            elif not hold:
                buy = yesterday
                hold=True
            yesterday = p
        if hold:
            total+=yesterday-buy
        return total
            

        pass

def test_ex1():
    prices = [7,1,5,3,6,4]
    ans = 7
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