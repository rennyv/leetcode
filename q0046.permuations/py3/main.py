class Solution:
    def permute(self, nums):
        res = []
        L = len(nums)
        if L == 1:
            return [nums.copy()]
        
        for i in nums:
            f = nums.pop(0)

            lis = self.permute(nums)

            for l in lis:
                l.append(f)
            
            res.extend(lis)

            nums.append(f)
        return res
        


def test_ex1():
    nums= [1,2,3]
    sol = Solution()
    print(sol.permute(nums))

test_ex1()