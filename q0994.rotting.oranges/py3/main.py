class Solution:
    def orangesRotting(self, grid) -> int:
        rows, cols = len(grid), len(grid[0])
        rotten, freshlen = set(), 0

        #load oranges
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    freshlen += 1
                
                elif grid[i][j] == 2:
                    rotten.add((i,j))
        
        #no fresh oranges escape
        if freshlen == 0: return 0

        minutes = 0
        #while there are fresh we need to keep going
        while freshlen > 0:
            newrotten = rotten.copy()
            for (i,j) in rotten:
                for di, dj in [[1,0], [0,1], [-1,0], [0,-1]]:
                    if -1<(i+di)<rows and -1<(j+dj)<cols:
                        if grid[i+di][j+dj] == 1:
                            grid[i+di][j+dj] = 2
                            freshlen -= 1
                            newrotten.add((i+di,j+dj))
            #if no new rotten then we have no connecting fresh to rotten
            if newrotten == rotten: return -1
            rotten = newrotten
            minutes += 1        

        return minutes
        
def test_ex1():
    sol = Solution()
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print(sol.orangesRotting(grid))

test_ex1()
