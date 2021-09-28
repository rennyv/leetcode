class Solution:
    def sortArrayByParityII(self, nums):
        L = len(nums)
        if(L == 0):
            return nums

        j = 1
        for i in range(0, L, 2):
            if(nums[i] % 2 == 1):
                while j < L and nums[j] % 2 == 1:
                    j += 2

                nums[i], nums[j] = nums[j], nums[i]

        return nums

def test_ex1():
    nums = [4,2,5,7]

    sol = Solution()

    print(sol.sortArrayByParityII(nums))

def test_ex1():
    nums = [4,2,6,8,3,9,5,7]

    sol = Solution()

    print(sol.sortArrayByParityII(nums))

test_ex1()