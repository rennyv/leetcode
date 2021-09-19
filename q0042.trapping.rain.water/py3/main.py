class Solution:
    def trap(self, height):
        L = len(height)
        if L < 3: return 0
        s = [0] * len(height)

        max_left = 0
        for i in range(L):
            max_left = max(max_left, height[i])
            s[i] = max_left - height[i]

        print(s)
        max_right = 0
        sum = 0
        for i in range(L,0,-1):
            max_right = max(max_right, height[i-1])
            s[i-1] = min(s[i-1], max_right-height[i-1])
            sum += s[i-1]
        
        return sum

        


def test_ex1():
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    ans = 6

    sol = Solution()
    assert ans == sol.trap(height)

def test_ex2():
    height = [4,2,0,3,2,5]
    ans = 9

    sol = Solution()
    assert ans == sol.trap(height)

test_ex1()