class Solution:
    def maxPower(self, s: str) -> int:
        max_ = 1
        curr_count = 0
        curr = ""
        for i in s:
            if not curr == i:
                curr = i
                curr_count = 1
            else:
                curr_count += 1
                max_ = max(max_, curr_count)
        
        return max_
        


def test_ex1():
    s = "leetcode"
    ans = 2

    sol = Solution()
    assert ans == sol.maxPower(s)

def test_ex2():
    s = "abbcccddddeeeeedcba"
    ans = 5

    sol = Solution()
    assert ans == sol.maxPower(s)

def test_ex3():
    s = "triplepillooooow"
    ans = 5

    sol = Solution()
    assert ans == sol.maxPower(s)

def test_ex4():
    s = "hooraaaaaaaaaaay"
    ans = 11

    sol = Solution()
    assert ans == sol.maxPower(s)

def test_ex5():
    s = "tourist"
    ans = 1

    sol = Solution()
    assert ans == sol.maxPower(s)

test_ex5()