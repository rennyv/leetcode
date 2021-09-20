class Solution:
    def numDecodings(self, s: str):
        dp = [0] * (len(s)+1)

        dp[0] = 1
        dp[1] = 0 if s[0]=='0' else 1

        for i in range(2, len(s)+1):
            one = int(s[i-1:i])
            two = int(s[i-2:i])
            if one >= 1:
                dp[i] += dp[i-1]
            if two >=10 and two<=26:
                dp[i] += dp[i-2]

        return dp[-1]
        

        


def test_ex1():
    s = "12"
    ans = 2

    sol = Solution()
    assert ans == sol.numDecodings(s)

def test_ex2():
    s = "226"
    ans = 3

    sol = Solution()
    assert ans == sol.numDecodings(s)

def test_ex3():
    s = "0"
    ans = 0

    sol = Solution()
    assert ans == sol.numDecodings(s)

def test_ex4():
    s = "06"
    ans = 0

    sol = Solution()
    assert ans == sol.numDecodings(s)

test_ex2()