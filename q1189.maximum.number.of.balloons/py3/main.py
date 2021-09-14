class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {}
        d['b'],d['a'],d['l'],d['o'],d['n'] = 0,0,0,0,0
        for i in text:
            if i in d:
                d[i] += 1
        
        return min(d['b'],d['a'],d['l']//2,d['o']//2, d['n'])



def test_ex1():
    text = "nlaebolko"
    ans = 1

    sol = Solution()
    assert ans == sol.maxNumberOfBalloons(text)

def test_ex2():
    text = "leetcode"
    ans = 0

    sol = Solution()
    assert ans == sol.maxNumberOfBalloons(text)

test_ex1()