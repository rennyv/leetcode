class Solution:
    def rob(self, nums):
        L = len(nums)

        if L < 4:
            return max(nums)

        def maxAmountRobbed(arr):
            dp = [0, arr[0]]
            for i in range(1, len(arr)):
                dp.append(max(dp[i], arr[i]+dp[i-1]))
            
            return dp[-1]
        
        v1 = maxAmountRobbed(nums[0:-1])
        v2 = maxAmountRobbed(nums[1:])

        return max(v1,v2)

def test_ex1():
    nums = [2,3,2]
    ans = 3
    
    sol = Solution()
    assert ans == sol.rob(nums)

def test_ex2():
    nums = [1,2,3,1]
    ans = 4
    
    sol = Solution()
    assert ans == sol.rob(nums)

def test_ex3():
    nums = [1,2,3]
    ans = 3
    
    sol = Solution()
    assert ans == sol.rob(nums)

def test_ex4():
    nums = [200,3,140,20,10]
    ans = 420
    
    sol = Solution()
    assert ans == sol.rob(nums)

test_ex4()