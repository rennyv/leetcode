class Solution:
    def reverseOnlyLetters(self, s):
        if len(s) < 2: return s
        l, r = 0, len(s)-1
        a = list(s)
        while r >= l:
            if a[l].isalpha() and a[r].isalpha():
                a[l], a[r] = a[r], a[l]
                l += 1
                r -= 1
            
            if not a[l].isalpha():
                l += 1
            if not a[r].isalpha():
                r -= 1
        return ''.join(a)

# Another style: Stack of Letters
        # letters = [c for c in S if c.isalpha()]
        # ans = []
        # for c in S:
        #     if c.isalpha():
        #         ans.append(letters.pop())
        #     else:
        #         ans.append(c)
        # return "".join(ans)



def test_ex1():
    sol = Solution()
    s = "ab-cd"
    assert sol.reverseOnlyLetters(s) == "dc-ba"

def test_ex2():
    sol = Solution()
    s = "a-bC-dEf-ghIj"
    assert sol.reverseOnlyLetters(s) == "j-Ih-gfE-dCba"

def test_ex3():
    sol = Solution()
    s = "Test1ng-Leet=code-Q!"
    assert sol.reverseOnlyLetters(s) == "Qedo1ct-eeLg=ntse-T!"

def test_ex4():
    sol = Solution()
    s = "T"
    assert sol.reverseOnlyLetters(s) == "T"

def test_ex5():
    sol = Solution()
    s = "Ta"
    assert sol.reverseOnlyLetters(s) == "aT"

test_ex1()