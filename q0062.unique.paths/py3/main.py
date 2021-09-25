class Solution:
    def uniquePaths(self, m, n):
        ans = [[0]*(m+1) for _ in range(n+1)]
        

        for i in range(1,n+1):
            for j in range(1,m+1):
                if i == 1 and j == 1: 
                    ans[i][j] = 1
                else:
                    ans[i][j] = ans[i-1][j] + ans[i][j-1] 
        return ans[n][m]


        


def test_ex1():
    m=3
    n=7
    ans = 28

    sol = Solution()
    assert ans == sol.uniquePaths(m,n)

def text_ex2():
    m=3
    n=2
    ans = 3

def test_ex3():
    m=7
    n=3
    ans = 28

    sol = Solution()
    assert ans == sol.uniquePaths(m,n)

def test_ex4():
    m=3
    n=3
    ans = 6

    sol = Solution()
    assert ans == sol.uniquePaths(m,n)

test_ex1()