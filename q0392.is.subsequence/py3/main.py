class Solution:
    def isSubsequence(self, s: str, t):
        if s == "": return True
        j = 0
        d = len(s)
        for _, c in enumerate(t):
            if c == s[j]:
                j += 1
                if j >= d:
                    return True
        return False

        

def test_ex1():
    s = "abc"
    t = "ahbgdc"
    ans = True

    sol = Solution()
    assert ans == sol.isSubsequence(s,t)

def test_ex2():
    s = "axc"
    t = "ahbgdc"
    ans = False

    sol = Solution()
    assert ans == sol.isSubsequence(s,t)

test_ex1()
