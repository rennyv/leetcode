class Solution:
    def reverseWords(self, s: str) -> str:
        swords = s.split(" ")
        ans = []
        for i in range(len(swords)-1, -1, -1):
            if swords[i] != '':
                ans.append(swords[i])
        return " ".join(ans)

        # one line answer ---- return ' '.join(reversed(s.split()))


def test_ex1():
    s = "the sky is blue"
    ans =  "blue is sky the" 

    sol = Solution()
    assert ans == sol.reverseWords(s)

def test_ex2():
    s = "  hello world  "
    ans = "world hello"

    sol = Solution()
    assert ans == sol.reverseWords(s)

def test_ex3():
    s = "a good   example"
    ans = "example good a"

    sol = Solution()
    assert ans == sol.reverseWords(s)

def test_ex4():
    s = "  Bob    Loves  Alice   "
    ans = "Alice Loves Bob"

    sol = Solution()
    assert ans == sol.reverseWords(s)

def test_ex5():
    s = "Alice does not even like bob"
    ans = "bob like even not does Alice"

    sol = Solution()
    assert ans == sol.reverseWords(s)

test_ex4()