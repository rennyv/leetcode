from typing import List
#from math import abs

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = set()

        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] < 0:
                result.add(idx + 1)
            else:
                nums[idx] *= -1
        
        return result
        
        
        # need to be constant memory size
        # d = {}
        # ans = set()
        # for n in nums:
        #     if n in d:
        #         ans.add(n)
        #     else:
        #         d[n] = True
        # return ans

def test_ex1():
    nums = [1]
    ans = []

    sol = Solution()
    print('ans: ', ans)
    print('sol:', sol.findDuplicates(nums))

def test_ex2():
    nums = [1,1,2]
    ans = [1]

    sol = Solution()
    print('ans: ', ans)
    print('sol:', sol.findDuplicates(nums))

def test_ex3():
    nums = [4,3,2,7,8,2,3,1]
    ans = [2,3]

    sol = Solution()
    print('ans: ', ans)
    print('sol:', sol.findDuplicates(nums))