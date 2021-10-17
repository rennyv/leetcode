import math

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [math.inf]*n

        for i in range(1, n+1):
            dp[i] = 1 + min(dp[i-j*j] for j in range(1,int(math.sqrt(n)+1)))
        return dp[-1]



def test_ex1():
    n = 12
    ans = 3

    sol = Solution()
    assert ans == sol.numSquares(n)

def test_ex2():
    n = 13
    ans = 2

    sol = Solution()
    assert ans == sol.numSquares(n)

test_ex2()


