class Solution:
    def nthUglyNumber(self, n):
        # DP cache
        dp = [0]*n
        # DP base case
        dp[0] = 1
        # DP step case
        i2 = i3 = i5 = 0
        for i in range(1, n):
            k = min(dp[i2]*2, dp[i3]*3, dp[i5]*5) # Next ugly number
            dp[i] = k
            if dp[i] == dp[i2]*2:
                i2 = i2+1
            if dp[i] == dp[i3]*3:
                i3 = i3+1
            if dp[i] == dp[i5]*5:
                i5 = i5+1
        return dp[n-1]





def test_ex1():
    n = 10
    ans = 12

    sol = Solution()
    assert ans == sol.nthUglyNumber(n)

def test_ex2():
    n = 1
    ans = 1
    
    sol = Solution()
    assert ans == sol.nthUglyNumber(1)

def test_ex3():
    n = 11
    ans = 15

    sol = Solution()
    assert ans == sol.nthUglyNumber(n)

test_ex3()