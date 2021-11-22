

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xb, yb, ans = f'{x:032b}', f'{y:032b}', 0

        ans = sum(i != j for i, j in zip(xb, yb))

        return ans


def test_ex1():
    x = 1
    y = 4
    ans = 2

    sol = Solution()

    assert ans == sol.hammingDistance(x,y)

def test_ex2():
    x = 3
    y = 1
    ans = 1

    sol = Solution()

    assert ans == sol.hammingDistance(x,y)

test_ex1()