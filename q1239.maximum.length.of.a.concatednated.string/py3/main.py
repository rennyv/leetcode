class Solution:
    def maxLength(self, arr):
        ans = 0
        L = len(arr)
        def hasDup(s):
            return len(s) != len(set(s))

        def backtracking(cur_s, index):
            nonlocal ans
            ans = max(ans, len(cur_s))
            for i in range(index, L):
                new_s = cur_s + arr[i]
                if not hasDup(new_s):
                    backtracking(new_s, i + 1)
        backtracking("",0)
        return ans


def test_ex1():
    arr = ["un","iq","ue"]
    ans = 4

    sol = Solution()
    assert ans == sol.maxLength(arr)

def test_ex2():
    arr = ["cha","r","act","ers"]
    ans = 6

    sol = Solution()
    assert ans == sol.maxLength(arr)

def test_ex3():
    arr = ["abcdefghijklmnopqrstuvwxyz"]
    ans = 26

    sol = Solution()
    assert ans == sol.maxLength(arr)