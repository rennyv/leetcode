from typing import NoReturn


class Solution:
    def numDistinct(self, s, t):
        cache = {}
        
        def dfs(i,j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i,j) in cache:
                return cache[(i,j)]

            if s[i] == t[j]:
                cache[(i,j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                cache[(i,j)] = dfs(i + 1, j)
            return cache[(i,j)]

        return dfs(0,0)

def test_ex1():
    s = "rabbbit"
    t = "rabbit"
    ans = 3

    sol = Solution()

    assert ans == sol.numDistinct(s,t)

def test_ex2():
    s = "babgbag"
    t = "bag"
    ans = 5

    sol = Solution()

    assert ans == sol.numDistinct(s,t)

test_ex1()