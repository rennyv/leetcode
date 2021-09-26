class Solution:
    def maximalSquare(self, matrix) -> int:
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0] * n for _ in range(m)]
        ans = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0": continue
                
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
                ans = max(ans, dp[i][j])
        return ans * ans


        

def test_ex1():
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    ans = 4

    sol = Solution()
    assert ans == sol.maximalSquare(matrix)

def test_ex2():
    matrix = [["0","1"],["1","0"]]
    ans = 1

    sol = Solution()
    assert ans == sol.maximalSquare(matrix)

test_ex1()