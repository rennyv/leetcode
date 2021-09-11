class Solution:
    def calculate(self, s: str) -> int:
        ans = 0
        sign = 1
        stack = []
        i = 0
        while i < len(s):
            #number
            if s[i].isdigit():
                num = 0
                while(i < len(s) and s[i].isdigit()):
                    num = num*10 + int(s[i])
                    i += 1
                ans += num*sign
                i -= 1
            # +
            elif s[i] == "+":
                sign = 1
            # -
            elif s[i] == "-":
                sign = -1
            # (
            elif s[i] == "(":
                stack.append(ans)
                stack.append(sign)
                ans = 0
                sign = 1
            # )
            elif s[i] == ")":
                ans = stack.pop() * ans
                ans += stack.pop()
            i += 1
        return ans


def test_ex1():
    s = "1 + 1"
    ans = 2
    sol = Solution()
    assert ans == sol.calculate(s)

def test_ex2():
    s = " 2-1 + 2 "
    ans = 3
    sol = Solution()
    assert ans == sol.calculate(s)

def test_ex3():
    s = "(1+(4+5+2)-3)+(6+8)"
    ans = 23
    sol = Solution()
    assert ans == sol.calculate(s)

def test_ex4():
    s = "2147483647"
    ans = 2147483647
    sol = Solution()
    assert ans == sol.calculate(s)

test_ex4()