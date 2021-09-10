
class Solution:
    def minimumTotal(self, triangle) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        
        for r in range(len(triangle)-2, -1, -1):
            for c in range(len(triangle[r])):
                a = triangle[r+1][c]
                b = triangle[r+1][c+1]
                triangle[r][c] += min(a,b)
        
        return triangle[0][0] 


def test_ex1():
    sol = Solution()
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    out = 11
    assert out == sol.minimumTotal(triangle)

def test_ex2():
    sol = Solution()
    triangle = [[-10]]
    out = -10
    assert out == sol.minimumTotal(triangle)
test_ex1()
