from sys import maxsize

class Solution:
    def minFallingPathSum(self, matrix):
        L = len(matrix[0])
        H = len(matrix)

        for y in range(H-2,-1,-1):
            for x in range(0,L):
                a = maxsize if x == 0 else matrix[y+1][x-1]
                b = matrix[y+1][x]
                c = maxsize if x == L-1 else matrix[y+1][x+1]
                matrix[y][x] += min(a,b,c) 
        return min(matrix[0])


        
        

def test_ex1():
   matrix = [[2,1,3],[6,5,4],[7,8,9]]
   ans = 13

   sol = Solution()
   assert ans == sol.minFallingPathSum(matrix) 

def test_ex2():
   matrix = [[-19,57],[-40,-5]]
   ans = -59

   sol = Solution()
   assert ans == sol.minFallingPathSum(matrix) 

def test_ex3():
   matrix = [[-48]]
   ans = -48

   sol = Solution()
   assert ans == sol.minFallingPathSum(matrix) 

test_ex3()