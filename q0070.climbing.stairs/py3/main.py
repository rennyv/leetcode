class Solution:
    def climbStairs(self, n):        
        if n == 1: return 1

        arr = [1,2]
        for i in range(2,n):
            arr.append(arr[i-1] + arr[i-2])
        
        return arr[n-1]


def test_ex1():
    sol = Solution()
    n = 2
    assert sol.climbStairs(n) == 2

def test_ex2():
    sol = Solution()
    n = 3
    assert sol.climbStairs(n) == 3

def test_ex3():
    sol = Solution()
    n = 5
    assert sol.climbStairs(n) == 8

test_ex3()