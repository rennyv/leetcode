
class Solution:
    def singleNumber(self, nums):
        el = nums[0]
        for i in range(1,len(nums)):
            el = el ^ nums[i]           #bitwise xor, the double number will cancel each other out leaving the odd number
            
        return el

def test_ex1():
    nums = [2,2,1]
    output = 1
    sol = Solution()
    assert output == sol.singleNumber(nums)


def test_ex2():
    nums = [4,1,2,1,2]
    output = 4
    sol = Solution()
    assert output == sol.singleNumber(nums)

test_ex2()