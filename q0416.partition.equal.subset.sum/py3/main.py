from typing import List
from functools import lru_cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum, i = sum(nums), 0
        @lru_cache
        def subsetSum(s):
            nonlocal i
            if s == 0: return True
            if i >= len(nums) or s < 0: return False
            i += 1
            ans = subsetSum(s-nums[i-1]) or subsetSum(s)
            i -= 1
            return ans
        return total_sum & 1 == 0 and subsetSum(total_sum // 2)

def test_ex1():
    nums = [1,5,11,5]
    
    sol = Solution()
    assert sol.canPartition(nums)

def test_ex2():
    nums = [1,2,3,5]
    
    sol = Solution()
    assert not sol.canPartition(nums)

test_ex1()
w