
class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        
        mod = 10 ** 9 + 7
        dp_full = [0 for _ in range(n)]
        dp_incomplete = [0 for _ in range(n)]
        
        dp_full[0] = 1
        dp_full[1] = 2
        dp_incomplete[1] = 2
        
        for i in range(2, n):
            dp_full[i] = dp_full[i-2] + dp_full[i-1] + dp_incomplete[i-1]
            dp_incomplete[i] = dp_full[i-2] * 2 + dp_incomplete[i-1]
        
        return dp_full[-1]%mod


def test_ex1():
    n = 3
    ans = 5
    
    sol = Solution()
    
    assert ans == sol.numTilings(n)
    
def test_ex2():
    n = 1
    ans = 1
    
    sol = Solution()
    