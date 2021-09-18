class Solution:
    def maxScoreSightseeingPair(self, values):
        p_num, max_ = values[0], 0

        for num in values[1:]:
            max_, p_num = max(max_, num + p_num - 1), max(p_num - 1, num)
        
        return max_
        
        # brute force times out
        # max_ = 0
        # for i in range(len(values)-1):
        #     for j in range(i+1,len(values)):
        #         max_ = max(max_, values[i] +values[j]+i-j)
        # return max_

def test_ex1():
    values = [8,1,5,2,6]
    ans = 11
    sol = Solution()

    assert ans == sol.maxScoreSightseeingPair(values)

def test_ex2():
    values = [1,2]
    ans = 2
    sol = Solution()

    assert ans == sol.maxScoreSightseeingPair(values)

def test_ex3():
    values = [2,2,2]
    ans = 3
    sol = Solution()

    assert ans == sol.maxScoreSightseeingPair(values)

test_ex1()