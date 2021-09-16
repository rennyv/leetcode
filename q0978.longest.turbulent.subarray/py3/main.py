class Solution:
    def maxTurbulenceSize(self, arr) -> int:
        inc = dec = result = 1
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                dec = inc + 1
                inc = 1
            elif arr[i] > arr[i - 1]:
                inc = dec + 1
                dec = 1
            else:
                inc = dec = 1
            result = max(result, max(dec, inc))
        return result

        

def test_ex1():
    arr = [9,4,2,10,7,8,8,1,9]
    ans = 5
    sol = Solution()

    assert ans == sol.maxTurbulenceSize(arr)

def test_ex2():
    arr = [4,8,12,16]
    ans = 2
    sol = Solution()

    assert ans == sol.maxTurbulenceSize(arr)

def test_ex3():
    arr = [100]
    ans = 1
    sol = Solution()

    assert ans == sol.maxTurbulenceSize(arr)

test_ex1()