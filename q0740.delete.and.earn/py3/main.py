class Solution:
    def deleteAndEarn(self, nums):
        #simalar to the house robbers (q0198, q0213) but we need to make the array
        nums.sort()
        n = nums[-1]
        new_nums = [0]*(n + 1)
        for k in nums:
            new_nums[k] += k       

        dp = [0, new_nums[0]]
 
        for i in range(1,n+1):
            dp.append(max(dp[i],new_nums[i]+dp[i-1]))
        return dp[-1]
 

def test_ex1():
    sol = Solution()
    nums = [3,4,2]
    ans = 6

    assert ans == sol.deleteAndEarn(nums)

def test_ex2():
    sol = Solution()
    nums = [2,2,3,3,3,4]
    ans = 9

    assert ans == sol.deleteAndEarn(nums)

def test_ex3():
    sol = Solution()
    nums = [3,3,3,4,2]
    ans = 9

    assert ans == sol.deleteAndEarn(nums)

test_ex3()