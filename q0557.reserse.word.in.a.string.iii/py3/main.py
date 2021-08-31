class Solution:
    def reverseWords(self, s) -> str:
        result = ""
        lb = 0
        for rb in range(len(s)):
            if s[rb] == " ":
                result += s[lb:rb][::-1] + " "
                lb = rb + 1
        result += s[lb:][::-1]
        return result
        #another solution: return " ".join([i[::-1] for i in s.split()])


sol = Solution()
s = "Let's take LeetCode contest"
ans = sol.reverseWords(s)
print(ans)


def test_ex1():
    sol = Solution()
    s = "Let's take LeetCode contest"
    target = "s'teL ekat edoCteeL tsetnoc"

    ans = sol.reverseWords(s)

    assert ans==target

def test_ex2():
    sol = Solution()
    s = "God Ding"
    target = "doG gniD"

    ans = sol.reverseWords(s)

    assert ans==target