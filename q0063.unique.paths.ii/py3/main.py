class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[-1][-1] == 1: return 0
        ans = [ [0] * (n+1) for _ in range(m+1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if obstacleGrid[i-1][j-1] == 1:
                    ans[i][j] = 0
                    continue
                if i == 1 and j == 1:
                    ans[i][j] = 1
                    continue
                ans[i][j] = ans[i-1][j] + ans[i][j-1]
        return ans[m][n]


def test_ex1():
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    ans = 2

    sol = Solution()    
    assert ans == sol.uniquePathsWithObstacles(obstacleGrid)

def test_ex2():
    obstacleGrid = [[0,1],[0,0]]
    ans = 1

    sol = Solution()    
    assert ans == sol.uniquePathsWithObstacles(obstacleGrid)

def test_ex3():
    obstacleGrid = [[0,0],[0,1]]
    ans = 0    
    sol = Solution()    
    assert ans == sol.uniquePathsWithObstacles(obstacleGrid)


test_ex3()