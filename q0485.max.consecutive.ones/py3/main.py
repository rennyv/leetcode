class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_ones = 0
        curr_max = 0

        for n in nums:
            if n == 1:
                curr_max += 1
                max_ones = max(max_ones, curr_max)
            else:
                curr_max = 0
        
        return max_ones
        

def test_ex1():
    nums = [1,1,0,1,1,1]
    ans = 3

    sol = Solution()
    assert ans == sol.findMaxConsecutiveOnes(nums)

def test_ex2():
    nums = [1,0,1,1,0,1]
    ans = 2

    sol = Solution()
    assert ans == sol.findMaxConsecutiveOnes(nums)    
