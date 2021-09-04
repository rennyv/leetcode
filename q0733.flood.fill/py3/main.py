class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        image[sr][sc] = newColor
        if sr>0 and image[sr-1][sc] == oldColor:
            self.floodFill(image, sr-1,sc,newColor)
        if sr<(len(image)-1) and image[sr+1][sc] == oldColor:
            self.floodFill(image, sr+1,sc,newColor)
        if sc>0 and image[sr][sc-1] == oldColor:
            self.floodFill(image, sr,sc-1,newColor)
        if sc<(len(image[sr])-1) and image[sr][sc+1] == oldColor:
            self.floodFill(image, sr,sc+1,newColor)
        
        return image

        # Solution Given
        # R, C = len(image), len(image[0])
        # color = image[sr][sc]
        # if color == newColor: return image
        # def dfs(r, c):
        #     if image[r][c] == color:
        #         image[r][c] = newColor
        #         if r >= 1: dfs(r-1, c)
        #         if r+1 < R: dfs(r+1, c)
        #         if c >= 1: dfs(r, c-1)
        #         if c+1 < C: dfs(r, c+1)

        # dfs(sr, sc)
        # return image


def test_ex1():
    sol = Solution()
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    newColor = 2

    print(sol.floodFill(image, sr,sc,newColor))

def test_ex2():
    sol = Solution()
    image = [[0,0,0],[0,0,0]]
    sr = 0
    sc = 0
    newColor = 2

    print(sol.floodFill(image, sr,sc,newColor))

def test_ex3():
    sol = Solution()
    image = [[0,0,0],[0,1,1]]
    sr = 1
    sc = 1
    newColor = 1

    print(sol.floodFill(image, sr,sc,newColor))

test_ex3()