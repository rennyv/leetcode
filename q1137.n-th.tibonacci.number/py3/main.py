class Solution:
    def tribonacci(self, n: int) -> int:
        cache = {}
        cache[0],cache[1],cache[2] = 0,1,1
        def t(num):
            if num in cache: return cache[num]
            a = t(num-1)
            cache[num-1] = a
            return a + t(num-2) + t(num-3)
        return t(n)

        


            

def test_ex1():
    sol = Solution()
    n = 0
    ans = 0
    assert ans == sol.tribonacci(n)

def test_ex2():
    sol = Solution()
    n = 1
    ans = 1
    assert ans == sol.tribonacci(n)

def test_ex3():
    sol = Solution()
    n = 2
    ans = 1
    assert ans == sol.tribonacci(n)

def test_ex4():
    sol = Solution()
    n = 3
    ans = 2
    assert ans == sol.tribonacci(n)

def test_ex5():
    sol = Solution()
    n = 4
    ans = 4
    assert ans == sol.tribonacci(n)

def test_ex6():
    sol = Solution()
    n = 25
    ans = 1389537
    assert ans == sol.tribonacci(n)

test_ex5()