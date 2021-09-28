class Solution:
    def wiggleMaxLength(self, nums):
        L = len(nums)
        # if L < 2:
        #     return L
        
        up = [0] * L
        down = [0] * L

        up[0], down[0] = 1,1

        for i in range(1,L):
            if nums[i] > nums[i-1]:
                up[i] = down[i-1] + 1
                down[i] = down[i-1]
            elif nums[i] < nums[i-1]:
                up[i] = up[i-1]
                down[i] = up[i-1] + 1
            else:
                up[i] = up[i-1]
                down[i] = down[i-1]
            
        return max(up[L-1], down[L-1])

def test_ex1():
    nums = [1,7,4,9,2,5]
    ans = 6

    sol = Solution()
    assert ans == sol.wiggleMaxLength(nums)

def test_ex2():
    nums = [1,17,5,10,13,15,10,5,16,8]
    ans = 7

    sol = Solution()
    assert ans == sol.wiggleMaxLength(nums)

def test_ex3():
    nums = [0,0]
    ans = 1

    sol = Solution()
    assert ans == sol.wiggleMaxLength(nums)

test_ex3()