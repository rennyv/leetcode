class Solution:

    def sortedSquares(self, nums):
        ans = []
        left, right = 0, len(nums)-1
        for i in range(0, right+1):
            lsq = nums[left] * nums[left]
            rsq = nums[right] * nums[right]

            if lsq > rsq:
                ans.insert(0, lsq)
                left = left + 1
            else:
                ans.insert(0, rsq)
                right = right - 1
			
        return ans






sol = Solution()
nums = [-4,-1,0,3,10]
ans = sol.sortedSquares(nums)
print("ans", ans)
