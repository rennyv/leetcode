class Solution:
    def isPowerOfTwo(self, n):
        if n <= 0: return False
        if n == 1: return True      
        for i in "{0:b}".format(n-1):
            if i == '0': return False
        return True


def test_ex1():
    sol = Solution()
    n=1
    assert sol.isPowerOfTwo(n)

def test_ex2():
    sol = Solution()
    n=16
    assert sol.isPowerOfTwo(n)

def test_ex3():
    sol = Solution()
    n=3
    assert not sol.isPowerOfTwo(n)

def test_ex4():
    sol = Solution()
    n=4
    assert sol.isPowerOfTwo(n)

def test_ex5():
    sol = Solution()
    n=5
    assert not sol.isPowerOfTwo(n)

test_ex5()