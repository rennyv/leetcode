class Solution:
    def breakPalindrome(self, palindrome):
        L = len(palindrome)
        if L == 1: return ""
        s = [char for char in palindrome]
        for i in range(L):
            j = L - 1 - i
            if j == i: continue
            if s[i] != 'a':
                s[i] = 'a'
                return ''.join(s)
        s[-1] = 'b'

        return ''.join(s)