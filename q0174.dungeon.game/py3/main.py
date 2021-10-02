from typing import List
from sys import maxsize

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])

        minHealth = [ [0] * (n+1) for _ in range(m+1)]

        for r in range(m, -1, -1):
            for c in range(n, -1, -1):
                if ((r == m -1 and c == n) or (r == m and c == n - 1)):
                    minHealth[r][c] = 1
                    continue
                
                if (r >= m or c >= n):
                    minHealth[r][c] = maxsize
                    continue

                minHealth[r][c] = min(minHealth[r][c+1], minHealth[r+1][c]) - dungeon[r][c]

                if (minHealth[r][c] <= 0): minHealth[r][c] = 1


        return minHealth[0][0]

def test_ex1():
   dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
   ans = 7

   sol = Solution()
   assert ans == sol.calculateMinimumHP(dungeon) 


test_ex1()