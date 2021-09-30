class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def lcs(n: int, m: int, t=dict()) -> int:
            if n==0 or m==0:
                return 0
            else:
                key = (n,m)
                if key not in t:
                    if text1[n-1] == text2[m-1]:
                        t[key] = lcs(n-1,m-1,t) + 1

                    else:
                        t[key] = max(lcs(n,m-1,t), lcs(n-1,m,t))
                        
            return t[key] 
        
        return lcs(len(text1), len(text2))

def test_ex1():
    text1 = "abcde"
    text2 = "ace"

    ans = 3

    sol = Solution()

    assert ans == sol.longestCommonSubsequence(text1, text2)

def test_ex2():
    text1 = "def"
    text2 = "ace"

    ans = 0

    sol = Solution()

    assert ans == sol.longestCommonSubsequence(text1, text2)

def test_ex3():
    text1 = "ace"
    text2 = "ace"

    ans = 3

    sol = Solution()

    assert ans == sol.longestCommonSubsequence(text1, text2)   

test_ex1()