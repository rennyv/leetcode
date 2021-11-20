#Binary Search
#Limits O(logn) and O(1)
from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r -l) - 1

            if nums[mid] == nums[mid + 1]:
                if (r-mid) % 2 == 0:
                    l = mid + 2
                else:
                    r = mid - 1
            elif nums[mid - 1] == nums[mid]:
                if (r - mid) % 2 == 0:
                    r = mid - 2
                else:
                    l = mid + 1
            else:
                return nums[mid]

        return nums[l]


def test_ex1():
    nums = [1,1,2,3,3,4,4,8,8]
    ans = 2

    sol = Solution()
    assert ans == sol.singleNonDuplicate(nums)

def test_ex2():
    nums = [3,3,7,7,10,11,11]
    ans = 10

    sol = Solution()
    assert ans == sol.singleNonDuplicate(nums)