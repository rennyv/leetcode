from typing import List
from collections import Counter

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = Counter(nums)
        ans = [i for i in range(1,len(nums)+1) if i not in s]
        
        return ans

        #Brute force takes too long
        # L = len(nums)
        # ans = []
        # for n in range(1,L+1):
        #     if not n in nums:
        #         ans.append(n)

        # return ans




def test_ex1():
    nums = [4,3,2,7,8,2,3,1]
    ans = [5,6]

    sol = Solution()

    print(ans)
    print(sol.findDisappearedNumbers(nums))
    assert ans == sol.findDisappearedNumbers(nums)


def test_ex2():
    nums = [1,1]
    ans = [2]

    sol = Solution()

    assert ans == sol.findDisappearedNumbers(nums)

test_ex1()