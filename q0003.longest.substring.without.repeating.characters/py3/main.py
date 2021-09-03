class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        count = 0
        a = ""
        for i in range(len(s)):
            if s[i] in a:                
                a = a[a.index(s[i])+1:] + s[i]
                count = len(a)
            else:
                count += 1
                max_length = max(max_length, count)
                a += s[i]
        return max_length

def test_ex1():
    sol = Solution()
    s = "abcabcbb"
    target = 3
    assert target == sol.lengthOfLongestSubstring(s)

def test_ex2():
    sol = Solution()
    s = "dvdf"
    target = 3
    assert target == sol.lengthOfLongestSubstring(s)

def test_ex3():
    sol = Solution()
    s = "bbbbbbbb"
    target = 1
    assert target == sol.lengthOfLongestSubstring(s)

def test_ex4():
    sol = Solution()
    s = "pwwkew"
    target = 3
    assert target == sol.lengthOfLongestSubstring(s)

def test_ex5():
    sol = Solution()
    s = "bbtablud"
    target = 6
    assert target == sol.lengthOfLongestSubstring(s)


        # queuing sample
        # queue = []
        # queueDict = {}
        # maxLen = 0
        
        # for char in s:
        #     while char in queueDict:
        #         k = queue.pop(0)
        #         queueDict.pop(k)
        #     queue.append(char)
        #     queueDict[char] = char
        #     queueLen = len(queue)
        #     if queueLen > maxLen:
        #         maxLen = queueLen
                
        # return maxLen