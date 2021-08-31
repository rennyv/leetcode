class Solution:
    def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

nums = [1,2,3,4,5,6,7]
k = 3

sol = Solution()
sol.rotate(nums, k)

print(nums)