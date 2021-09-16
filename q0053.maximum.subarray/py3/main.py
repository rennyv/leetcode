from sys import maxsize

class Solution:
    def maxSubArray(self, nums):
        s1= 0 
        m1= nums[0]         
        for i in nums:            
            if s1<0 :                
                s1=0 
            
            s1+= i 
            m1 = max(s1,m1) 
    
        return m1

def test_ex1():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    ans = 6
    sol = Solution()

    assert ans == sol.maxSubArray(nums)

def test_ex2():
    nums = [1]
    ans = 1
    sol = Solution()

    assert ans == sol.maxSubArray(nums)

def test_ex3():
    nums = [5,4,-1,7,8]
    ans = 23
    sol = Solution()

    assert ans == sol.maxSubArray(nums)

def test_ex4():
    nums = [1,2]
    ans = 3
    sol = Solution()

    assert ans == sol.maxSubArray(nums)

test_ex1()