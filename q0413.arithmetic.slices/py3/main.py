class Solution:
    def numberOfArithmeticSlices(self, nums):
        L = len(nums)
        if L < 3: return 0

        dp = [0] * L
        sum = 0
        for i in range(2,L):
            if((nums[i]-nums[i-1])==(nums[i-1]-nums[i-2])):
                dp[i]=dp[i-1]+1
            else:
                dp[i]=0
            sum+=dp[i]
        return sum



def test_ex1():
   nums = [1,2,3,4]
   ans = 3

   sol = Solution()
   assert ans == sol.numberOfArithmeticSlices(nums)

def test_ex2():
    nums = [1]
    ans = 0

    sol = Solution()
    assert ans == sol.numberOfArithmeticSlices(nums)

test_ex2()