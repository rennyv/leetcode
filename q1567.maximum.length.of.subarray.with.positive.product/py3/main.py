
class Solution:
    def getMaxLen(self, nums):
        positive = negative = 0
        result = 0

        for n in nums:
            if n == 0:
                positive = negative = 0
            elif n > 0:
                positive += 1
                negative = 0 if negative == 0 else negative+1
            else:
                temp = positive
                positive = 0 if negative == 0 else negative+1
                negative = temp + 1
            result = max(result, positive)
        return result
        
def test_ex1():
    nums = [1,-2,-3,4]
    ans = 4
    sol = Solution()

    assert ans == sol.getMaxLen(nums)

def test_ex2():
    nums = [0,1,-2,-3,-4]
    ans = 3
    sol = Solution()

    assert ans == sol.getMaxLen(nums)

def test_ex3():
    nums = [-1,-2,-3,0,1]
    ans = 2
    sol = Solution()

    assert ans == sol.getMaxLen(nums)

def test_ex4():
    nums = [-1,2]
    ans = 1
    sol = Solution()

    assert ans == sol.getMaxLen(nums)

def test_ex5():
    nums = [1,2,3,5,-6,4,0,10]
    ans = 4
    sol = Solution()

    assert ans == sol.getMaxLen(nums)
