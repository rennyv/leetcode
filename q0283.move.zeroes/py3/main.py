class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in range(len(nums)):
            el = nums[i]
            if el != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
        


sol = Solution()

nums = [0,1,0,3,12]
print(nums)
sol.moveZeroes(nums)
print(nums)  