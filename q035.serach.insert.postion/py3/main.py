class Solution:
    def searchInsert(self, nums, target) -> int:
        l, r = 0, len(nums)-1
        while l < r and r >= 0:
            m = l + (r - l)//2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return r if nums[r] >= target and r >= 0 else r+1

        


def test_ex1():
    sol = Solution()
    nums = [1,3,5,6]
    target = 5
    
    assert sol.searchInsert(nums, target) == 2

def test_ex2():
    sol = Solution()
    nums = [1,3,5,6]
    target = 2
    
    assert sol.searchInsert(nums, target) == 1

def test_ex3():
    sol = Solution()
    nums = [1,3,5,6]
    target = 7
    
    assert sol.searchInsert(nums, target) == 4

def test_ex4():
    sol = Solution()
    nums = [1,3,5,6]
    target = 0
    
    assert sol.searchInsert(nums, target) == 0

def test_ex5():
    sol = Solution()
    nums = [1]
    target = 0
    
    assert sol.searchInsert(nums, target) == 0
