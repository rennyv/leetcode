from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        lo = 0
        mid = hi = len(nums) - 1
        while lo <= mid:
            if   nums[mid] == 0:
                nums[lo], nums[mid] = nums[mid], nums[lo]
                lo += 1
            elif nums[mid] == 1:
                mid -= 1
            elif nums[mid] == 2:
                nums[mid], nums[hi] = nums[hi], nums[mid]
                mid -= 1
                hi -= 1

def test_ex1():
    nums = [2,0,2,1,1,0]
    ans = [0,0,1,1,2,2]

    sol = Solution()
    assert ans == nums
def test_ex2():
    nums = [2,0,1]
    ans = [0,1,2]

    sol = Solution()
    assert ans == sol.sortColors(nums)

def test_ex3():
    nums = [0]
    ans = [0]

    sol = Solution()
    assert ans == sol.sortColors(nums)

def test_ex4():
    nums = [1]
    ans = [1]

    sol = Solution()
    assert ans == sol.sortColors(nums)

test_ex1()