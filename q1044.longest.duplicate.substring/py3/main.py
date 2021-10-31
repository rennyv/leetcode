class Solution:
    def longestDupSubstring(self, s: str) -> str:
        results = set()
        window = len(s)//2
        largest = ""

        while window > len(largest):
            for right in range(window, len(s)+1):
                substr = s[right-window:right]
                if substr in results:
                    if len(substr) > len(largest):
                        largest = substr
                        window += (len(s)-window)//2+1
                        results.clear()
                        continue
                else:
                    results.add(substr)
            else:
                if window == len(largest) + 1:
                    break
                window = max(window//2, len(largest)+1)
        return largest


def test_ex1():
    s = "banana"
    ans = "ana"

    sol = Solution()
    assert ans == sol.longestDupSubstring(s)

def test_ex2():
    s = "abcd"
    ans = ""

    sol = Solution()
    assert ans == sol.longestDupSubstring(s)

test_ex2()