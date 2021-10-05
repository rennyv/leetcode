from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if(grid[i][j]==1):
                    count += 4
                    if i>0 and grid[i-1][j] == 1: count -= 2
                    if j>0 and grid[i][j-1] == 1: count -= 2
        return count


def test_ex1():
    grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    ans = 16

    sol = Solution()
    assert ans == sol.islandPerimeter(grid)

def test_ex2():
    grid = [[1]]
    ans = 4

    sol = Solution()
    assert ans == sol.islandPerimeter(grid)

def test_ex3():
    grid = [[1,0]]
    ans = 4

    sol = Solution()
    assert ans == sol.islandPerimeter(grid)
