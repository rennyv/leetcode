from sys import maxsize
class Solution:
    def updateMatrix(self, mat):
        rows = len(mat)
        if rows == 0: return mat        
        cols = len(mat[0])

        dist =  [ [ maxsize  for y in range(cols)] for x in range(rows) ]

        # start left top and move down
        for i in range(rows):
            for j in range(cols):
                if (mat[i][j] == 0):
                    dist[i][j] = 0
                else:
                    if (i > 0):
                        dist[i][j] = min(dist[i][j], dist[i -1][j] + 1)
                    if(j > 0):
                        dist[i][j] = min(dist[i][j], dist[i][j -1] + 1)

        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                if  i < (rows -1):
                    dist[i][j] = min(dist[i][j], dist[i +1][j] + 1)
                if j < (cols-1):
                    dist[i][j] = min(dist[i][j], dist[i][j +1] + 1)

        return dist


def test_ex1():
    sol = Solution()
    mat = [[0,0,0],[0,1,0],[0,0,0]]
    print(sol.updateMatrix(mat))

test_ex1()