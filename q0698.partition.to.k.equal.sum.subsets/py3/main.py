from functools import lru_cache

class Solution:
    def canPartitionKSubsets(self, nums, k):
        subsetSum, remain = divmod(sum(nums), k)
        if max(nums) > subsetSum or remain > 0: 
            return False  # Prune since we can't divide `nums` into subsets where each sums is equal to `subsetSum`
        n = len(nums)

        @lru_cache(None)
        def dp(mask):
            if mask == 0: return 0
            for i in range(n):
                if (mask >> i) & 1:
                    newMask = mask ^ (1 << i)
                    remain = dp(newMask)
                    if remain == -1: continue  # Skip case can't divide by using `newMask`
                    if remain + nums[i] <= subsetSum:
                        return (remain + nums[i]) % subsetSum
            return -1

        return dp((1 << n) - 1) == 0

def test_ex1():
    nums = [4,3,2,3,5,2,1]
    k = 4

    sol = Solution()
    assert sol.canPartitionKSubsets(nums, k)

def test_ex2():
    nums = [1,2,3,4]
    k = 3

    sol = Solution()
    assert not sol.canPartitionKSubsets(nums, k)
    