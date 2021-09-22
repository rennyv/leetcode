class Solution:
    def generate(self, numRows):
        t = [[1]]
        if numRows == 1:
            return t
        for i in range(2,numRows+1):
            newRow = [1] * i
            for n in range(1,i-1):
                newRow[n] = t[-1][n-1]+t[-1][n]
            t.append(newRow)
        return t



def test_ex1():
    numRows = 5
    ans = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

    sol = Solution()
    print(ans)
    print(sol.generate(numRows))

def test_ex2():
    numRows = 2
    ans = [[1],[1,1]]

    sol = Solution()
    print(ans)
    print(sol.generate(numRows))

def test_ex3():
    numRows = 1
    ans = [[1]]

    sol = Solution()
    print(ans)
    print(sol.generate(numRows))

test_ex3()