from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visit = set()
        #find all special points
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    visit.add((i, j))
                elif grid[i][j] == 1:
                    start = (i,j)
                elif grid[i][j] == 2:
                    end = (i,j)
                    visit.add((i, j))
        
        def backtrack(x,y,visit):
            if (x,y) == end:
                return len(visit) == 0
            result = 0

            choices = [(-1,0), (1,0), (0,-1),(0,1)]

            for x1, y1 in choices:
                i, j = x+x1, y+y1
                if (i, j) in visit:
                    visit.remove((i, j))
                    result += backtrack(i, j, visit)
                    visit.add((i, j))
            return result

        return backtrack(start[0], start[1], visit)


def test_ex1():
    grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    ans = 2

    sol = Solution()
    assert ans == sol.uniquePathsIII(grid)

def test_ex2():
    grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
    ans = 4
     
    sol = Solution()
    assert ans == sol.uniquePathsIII(grid)

def test_ex3():
    grid = [[0,1],[2,0]]
    ans = 0

    sol = Solution()
    assert ans == sol.uniquePathsIII(grid)

test_ex1()