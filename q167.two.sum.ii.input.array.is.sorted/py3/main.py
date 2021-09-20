class Solution:
    def twoSum(self, numbers, target):
        l = 0
        r = len(numbers)-1
        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l+1,r+1]


sol = Solution()

numbers = [2,7,11,15]
target = 9

ans = sol.twoSum(numbers, target)
print(ans)
