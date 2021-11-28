'''
O(n+m)  2 pointers
'''
from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        N = len(firstList)
        M = len(secondList)
        ret = []

        n = 0
        m = 0

        while n<N and m<M:
            s1 = firstList[n][0]
            e1 = firstList[n][1]

            s2 = secondList[m][0]
            e2 = secondList[m][1]

            if s1 <= s2 <= e1 or s2 <= s1 <= e2:
                ret.append([
                    max(s1,s2), min(e1,e2)
                ])

                if e1 >= e2:
                    m += 1
                else:
                    n += 1
            elif e1<s2:
                n+=1
            else:
                m+=1
        return ret

def test_ex1():
    firstList = [[0,2],[5,10],[13,23],[24,25]]
    secondList = [[1,5],[8,12],[15,24],[25,26]]
    ans = [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

    sol = Solution()
    assert ans == sol.intervalIntersection(firstList, secondList)

def test_ex2():
    firstList = []
    secondList = [[1,5],[8,12],[15,24],[25,26]]
    ans = []

    sol = Solution()
    assert ans == sol.intervalIntersection(firstList, secondList)

def test_ex3():
    firstList = [[0,2],[5,10],[13,23],[24,25]]
    secondList = []
    ans = []

    sol = Solution()
    assert ans == sol.intervalIntersection(firstList, secondList)

def test_ex4():
    firstList = [[1,7]]
    secondList = [[3,10]]
    ans = [[3,7]]

    sol = Solution()
    assert ans == sol.intervalIntersection(firstList, secondList)