from sys import maxsize

class Solution:
    def jump(self, nums) -> int:
        L = len(nums)
        if L == 1: return 0
        dp = [maxsize] * L
        dp[0] = 0
        for i in range(L-1):
            far = i+nums[i]
            if far >= L-1:
                return dp[i]+1
            for j in range(i+1, min(L, far+1)):
                dp[j] = min(dp[j], dp[i] + 1)


def test_ex1():
   nums = [2,3,1,1,4]

   sol = Solution()
   assert 2 == sol.jump(nums) 

def test_ex2():
   nums = [2,3,0,1,4]

   sol = Solution()
   assert 2 == sol.jump(nums)

test_ex1()