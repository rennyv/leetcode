from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #One-pass hash O(n)
        L = len(nums)
        hash = {}

        for i in range(L):
            c = target - nums[i]
            if c in hash:
                return [hash[c], i]
            hash[nums[i]] = i

        # Brute-force O(n^2)
        # L = len(nums)
        # for i in range(L):
        #     for j in range(i+1,L):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]



def test_ex1():
    nums = [2,7,11,15]
    target = 9

    ans = [0,1]

    sol = Solution()
    assert ans == sol.twoSum(nums, target)

def test_ex2():
    nums = [3,2,4]
    target = 6
    ans = [1,2]

    sol = Solution()
    assert ans == sol.twoSum(nums, target)

def test_ex3():
    nums = [3,3]
    target = 6
    ans = [0,1]

    sol = Solution()
    assert ans == sol.twoSum(nums, target)