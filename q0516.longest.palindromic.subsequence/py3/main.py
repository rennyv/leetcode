class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        # `pal[i][j]` is the longest palindromic subsequence's length in the substring `s[i:j + 1]`.
        pal = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            pal[i][i] = 1

        for i in range(len(s) - 2, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    # Both two letters can be contained.
                    pal[i][j] = pal[i + 1][j - 1] + 2
                else:
                    # Only choose one letter.
                    pal[i][j] = max(pal[i + 1][j], pal[i][j - 1])
        return pal[0][-1]
    
def test_ex1():
   s = "bbbab"
   ans = 4

   sol = Solution()
   assert ans == sol.longestPalindromeSubseq(s) 

test_ex1()