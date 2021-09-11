class Solution:
    def fib(self, n: int) -> int:
        if n < 2: return n
        dp = [0,1]
        
        while len(dp) <= n:
            dp.append(dp[-1]+dp[-2])
        return dp[-1]

# Recursive:
        # def f(num):
        #     if num==0:
        #         return 0
        #     elif num == 1:
        #         return 1
        #     return f(num-1)+f(num-2)
        # return f(n)

def test_ex1():
    sol = Solution()
    n=2
    output = 1
    assert output == sol.fib(n)
    
def test_ex2():
    sol = Solution()
    n=3
    output = 2
    assert output == sol.fib(n)

def test_ex3():
    sol = Solution()
    n=4
    output = 3
    assert output == sol.fib(n)

def test_ex4():
    sol = Solution()
    n=0
    output = 0
    assert output == sol.fib(n)

test_ex3()