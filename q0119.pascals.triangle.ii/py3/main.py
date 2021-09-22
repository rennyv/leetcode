class Solution:
    def getRow(self, rowIndex):
        t = [1]
        if rowIndex == 0: return t

        for i in range(0,rowIndex):
            newRow = [1] * (len(t)+1)
            for n in range(1,i+1):
                newRow[n] = t[n-1]+t[n]
            t = newRow
        return t


def test_ex1():
    rowIdx = 4
    ans = [1,4,6,4,1]

    sol = Solution()
    print(ans)
    print(sol.getRow(rowIdx))

def test_ex2():
    rowIdx = 1
    ans = [1,1]

    sol = Solution()
    print(ans)
    print(sol.getRow(rowIdx))

def test_ex3():
    rowIdx = 0
    ans = [1]

    sol = Solution()
    print(ans)
    print(sol.getRow(rowIdx))

test_ex3()