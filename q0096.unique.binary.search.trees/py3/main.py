class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 2: return n

        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2

        for i in range(3,n+1):
            for j in range(1,i+1):
                dp[i] += dp[j-1]*dp[i-j]
        
        return dp[-1]

def test_ex1():
    n = 3
    ans = 5

    sol = Solution()
    assert ans == sol.numTrees(n)

def test_ex2():
    n = 1
    ans = 1

    sol = Solution()
    assert ans == sol.numTrees(n)

test_ex1()

