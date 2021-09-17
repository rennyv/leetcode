class Solution:
    def spiralOrder(self, matrix):
        if len(matrix)==1:
            return matrix[0]
        else:
            ans = []
            ans.extend(matrix[0])
            del matrix[0]
            while len(matrix)>1:
                matrix = list(map(list, zip(*matrix)))
                matrix = matrix[::-1]
                ans.extend(matrix[0])
                del matrix[0]
            if len(matrix)>0:
                ans.extend(matrix[0][::-1])
            return ans


def test_ex():
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    sol = Solution()
    ans = "1,2,3,6,9,8,7,4,5"

    assert ans == ",".join(str(x) for x in sol.spiralOrder(matrix))


def test_ex2():
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    ans = "1,2,3,4,8,12,11,10,9,5,6,7"
    sol = Solution()

    assert ans == ",".join(str(x) for x in sol.spiralOrder(matrix))

test_ex2()
