class Solution:
    def islandSearch(grid, r,c):
        size = 0
        if grid[r][c] == 0:
            return 0
            if grid[r][c] == 1:                
                grid[r][c] = 0
                if r > 0: size += dfs(r-1,c)
                if r+1 < R: size += dfs(r+1,c)
                if c > 0: size += dfs(r,c-1)
                if c+1 < C: size += dfs(r,c+1)
                return size +1
    
    
    def maxAreaOfIsland(self, grid) -> int:
        R, C = len(grid), len(grid[0])
        max_size = 0;
        
        def dfs(r,c):
            size = 0
            if grid[r][c] == 1:                
                grid[r][c] = 0
                if r > 0: size += dfs(r-1,c)
                if r+1 < R: size += dfs(r+1,c)
                if c > 0: size += dfs(r,c-1)
                if c+1 < C: size += dfs(r,c+1)
                return size +1
            else:
                return size

        for x in range(R):
            for y in range(C):
                if grid[x][y] == 1:
                    max_size = max(max_size, dfs(x,y))
        
        return max_size

        # def dfs(r, c):
        #     if image[r][c] == color:
        #         image[r][c] = newColor
        #         if r >= 1: dfs(r-1, c)
        #         if r+1 < R: dfs(r+1, c)
        #         if c >= 1: dfs(r, c-1)
        #         if c+1 < C: dfs(r, c+1)

    
def test_ex1():
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,1,1,0,1,0,0,0,0,0,0,0,0],
         [0,1,0,0,1,1,0,0,1,0,1,0,0],
         [0,1,0,0,1,1,0,0,1,1,1,0,0],
         [0,0,0,0,0,0,0,0,0,0,1,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,0,0,0,0,0,0,1,1,0,0,0,0]]

    sol = Solution()
    print(sol.maxAreaOfIsland(grid))

def test_ex2():
    grid = [[0,0,0,0,0,0]]
    sol = Solution()
    print(sol.maxAreaOfIsland(grid))

def test_ex3():
    grid = [[0,0,1,0,0,0]]
    sol = Solution()
    print(sol.maxAreaOfIsland(grid))

test_ex1()