class NumMatrix:

    def __init__(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        
        self.ps = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                self.ps[i][j] = matrix[i-1][j-1] + self.ps[i-1][j] + self.ps[i][j-1] - self.ps[i-1][j-1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.ps[row2+1][col2+1] - self.ps[row1][col2+1] - self.ps[row2+1][col1] + self.ps[row1][col1]
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

def test_ex1():
    matrix =[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]] 
    
    sol = NumMatrix(matrix)


    ans = 8
    r1, c1, r2, c2 = 2,1,4,3
    assert ans == sol.sumRegion(r1,c1,r2,c2)

    ans2= 11
    r1, c1, r2, c2 = 1,1,2,2
    assert ans2 == sol.sumRegion(r1,c1,r2,c2)

    ans3 = 12
    r1, c1, r2, c2 = 1,2,2,4
    assert ans2 == sol.sumRegion(r1,c1,r2,c2)

test_ex1()
    