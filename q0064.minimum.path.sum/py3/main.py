from sys import maxsize
class Solution:
    def minPathSum(self,grid):
        m = len(grid)
        n = len(grid[0])

        ans = [[maxsize] * (n+1) for _ in range(m+1)]
        ans[1][1] = grid[0][0]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if i == 1 and j == 1: continue
                ans[i][j] = min(ans[i-1][j], ans[i][j-1]) + grid[i-1][j-1]

        return ans[-1][-1]

def test_ex1():
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    ans = 7

    sol = Solution()
    assert ans == sol.minPathSum(grid)

def test_ex2():
    grid = [[1,2,3],[4,5,6]]
    ans = 12

    sol = Solution()
    assert ans == sol.minPathSum(grid)

test_ex1()