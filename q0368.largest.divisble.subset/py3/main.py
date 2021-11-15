from typing import List
import collections
from functools import lru_cache

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n= len(nums)
        
        if n==0:return []
        
        nums.sort()
        
        dp=[ [i] for i in nums]
        
        for i in range(n):
            for j in range(i):
                
                if nums[i]%nums[j]==0 and len(dp[j])+1 > len(dp[i]):
                    
                    dp[i] = dp[j]+[nums[i]]
        
        return max(dp, key=len)


def test_ex1():
    nums = [1,2,3]
    ans = [1,2]

    sol = Solution()
    
    print(ans)
    print(sol.largestDivisibleSubset(nums))

def test_ex1():
    nums = [1,2,4,8]
    ans = [1,2,4,8]

    sol = Solution()
    
    print(ans)
    print(sol.largestDivisibleSubset(nums))

test_ex1()