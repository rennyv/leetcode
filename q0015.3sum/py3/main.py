from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        Set = set()
        nums.sort()

        L=len(nums)

        for i in range(L):
            j=i+1
            k=L-1

            while(j<k):
                sum=nums[i]+nums[j]+nums[k]
                if sum==0:
                    Set.add((nums[i],nums[j],nums[k]))
                    k=k-1
                    j=j+1
                elif sum>0:
                    k=k-1                    
                else:
                    j=j+1                    
        return [list(i) for i in Set]