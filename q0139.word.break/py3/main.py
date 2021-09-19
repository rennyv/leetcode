import functools

class Solution:
    def wordBreak(self, s, wordDict):
        @functools.lru_cache(None)
        def wordBreak_helper(start,end):
            if s[start:end] in wordDict:
                return True
            
            for i in range(start+1, end):
                if s[start:i] in wordDict and wordBreak_helper(i,end):
                    return True
            return False
        
        return wordBreak_helper(0,len(s))

#brute force - too slow
        # if s in wordDict: return True
        
        # l = ''
        # for i in s:
        #     l += i
        #     if l in wordDict:
        #        if self.wordBreak(s[len(l):], wordDict):
        #            return True
        # return False


def test_ex1():
    s = "leetcode"
    wordDict = ["leet","code"]

    sol = Solution()

    assert sol.wordBreak(s, wordDict)

def test_ex2():
    s = "applepenapple"
    wordDict = ["apple","pen"]

    sol = Solution()

    assert sol.wordBreak(s, wordDict)

def test_ex3():
    s = "catsandog"
    wordDict = ["cats","dog","sand","and","cat"]

    sol = Solution()

    assert not sol.wordBreak(s, wordDict)

test_ex3()